import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService, DataSet } from '../app.service';
import { interval, Subscription } from 'rxjs';
import { takeWhile } from 'rxjs/operators';
import { GA } from '../model/GA';

@Component({
  selector: 'app-experiment',
  templateUrl: './experiment.component.html',
  styleUrls: ['./experiment.component.css']
})
export class ExperimentComponent implements OnInit {
  id: Number;
  dataset: DataSet;
  data: GA;
  simulate: boolean;
  simulationSubscription: Subscription;
  loadingSubscription: Subscription;
  loading: string;

  constructor(private appSerivce: AppService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.id = +this.route.parent.snapshot.paramMap.get('id');
    this.route.paramMap.subscribe(params => {
      this.dataset = DataSet[params.get('dataset').toUpperCase()];
      this.init();
      this.updateComponent();
    });
  }

  init(): void {
    this.simulate = false;
    this.loading = '';
    if (this.simulationSubscription) {
      this.simulationSubscription.unsubscribe();
    }
    if (this.loadingSubscription) {
      this.loadingSubscription.unsubscribe();
    }
    if (this.data) {
      this.data.reset();
    }
  }

  updateComponent(): void {
    this.appSerivce.getData(this.id, this.dataset).subscribe(data => {
      this.data = new GA(data);
      console.log('GA Data', this.data);
    });
  }

  startSimulation(): void {
    this.init();
    this.simulate = true;

    this.simulationSubscription = interval(this.appSerivce.getInterval())
      .pipe(takeWhile(() => this.data.hasMoreGenerations()))
      .subscribe(() => {
        this.data.moveNext();
      });
    
    this.loadingSubscription = interval(150)
    .pipe(takeWhile(() => this.data.hasMoreGenerations()))
    .subscribe(() => {
      let maxLoad = '...........';
      let dots = (this.loading.match(/\./g) || []).length;
      dots = (dots + 1) % maxLoad.length; 
      console.log(this.loading, dots);
      this.loading = maxLoad.substr(0, dots);
    });
  }

  ngOnDestroy() {
    if (this.simulationSubscription) {
      this.simulationSubscription.unsubscribe();
    }
    if (this.loadingSubscription) {
      this.loadingSubscription.unsubscribe();
    }
  }

}
