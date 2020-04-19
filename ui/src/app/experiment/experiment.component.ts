import { Component, OnInit, ChangeDetectorRef, ViewChild, ElementRef, TemplateRef } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService, DataSet } from '../app.service';
import { interval, Subscription } from 'rxjs';
import { takeWhile } from 'rxjs/operators';
import { GA } from '../model/GA';
import { MemberChartComponent } from '../member-chart/member-chart.component';

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
  @ViewChild(MemberChartComponent, { static: false }) memberChartComponent: MemberChartComponent;

  constructor(private appSerivce: AppService, private route: ActivatedRoute,
              private ref: ChangeDetectorRef) { }

  ngOnInit() {
    this.id = +this.route.parent.snapshot.paramMap.get('id');
    this.ref.detach();
    this.route.paramMap.subscribe(params => {
      this.dataset = DataSet[params.get('dataset').toUpperCase()];
      this.init();
      this.updateComponent();
    });
  }

  init(): void {
    this.simulate = false;
    if (this.simulationSubscription) {
      this.simulationSubscription.unsubscribe();
    }
    if (this.data) {
      this.data.reset();
    }
  }

  updateComponent(): void {
    this.appSerivce.getData(this.id, this.dataset).subscribe(data => {
      this.data = new GA(data);
      console.log('GA Data', this.data);
      this.ref.detectChanges();
    });
  }

  startSimulation(): void {
    this.init();
    this.simulate = true;
    this.ref.detectChanges();

    this.simulationSubscription = interval(this.appSerivce.getInterval())
      .pipe(takeWhile(() => this.data.hasMoreGenerations()))
      .subscribe(() => {
        this.data.moveNext();
        this.memberChartComponent.updateChart();
        this.ref.detectChanges();
      });
  }

  ngOnDestroy() {
    if (this.simulationSubscription) {
      this.simulationSubscription.unsubscribe();
    }
  }

}
