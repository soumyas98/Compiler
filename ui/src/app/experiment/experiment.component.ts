import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService, DataSet } from '../app.service';
import { interval, Subscription } from 'rxjs';
import { takeWhile } from 'rxjs/operators';

@Component({
  selector: 'app-experiment',
  templateUrl: './experiment.component.html',
  styleUrls: ['./experiment.component.css']
})
export class ExperimentComponent implements OnInit {
  id: Number;
  dataset: DataSet;
  data: any;
  simulate: boolean;
  simulationSubscription: Subscription;
  currentGen: number;
  currentMem: number;

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
    this.currentGen = 0;
    this.currentMem = 0;
    if (this.simulationSubscription) {
      this.ngOnDestroy();
    }
  }

  updateComponent(): void {
    this.appSerivce.getData(this.id, this.dataset).subscribe(data => {
      this.data = data;
      console.log(this.data);
    });
  }

  startSimulation(): void {
    this.simulate = true;
    const generations = this.data['generation-count'];
    const population = this.data['population'];

    this.simulationSubscription = interval(this.appSerivce.getInterval())
      .pipe(takeWhile(() => this.currentGen < generations))
      .subscribe(() => {
        ++this.currentMem;
        if (this.currentMem > population) {
          this.currentMem = 0;
          ++this.currentGen;
        }
        console.log(this.currentGen, this.currentMem);
      });
  }

  ngOnDestroy() {
    this.simulationSubscription.unsubscribe();
  }

}
