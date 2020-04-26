import { Component, OnInit } from '@angular/core';
import { AppService, DataSet } from '../app.service';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';
import { BenchMark } from '../model/BenchMark';

@Component({
  selector: 'app-conclusion',
  templateUrl: './conclusion.component.html',
  styleUrls: ['./conclusion.component.css']
})
export class ConclusionComponent implements OnInit {
  benchMarks: BenchMark[] = new Array(4);
  pgmNames: string[] = [
    'Basic Math', 'Bit Count', 'Quick Sort', 'Susan'
  ];
  chart: any;

  constructor(private appService: AppService) { 
  }

  ngOnInit() {
    for (let i = 0; i < 4; ++i) {
      this.appService.getData(i + 1, DataSet.SMALL).subscribe(data => {
        this.benchMarks[i] = (new GA(data)).benchmark;
        if (i == 3) {
          this.initChart();
        }
      });
    }
  }

  initChart(): void {
    let data = this.getData();

    this.chart = new CanvasJS.Chart("conclusionChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Programs',
      },
      axisY: {
        title: 'Execution time',
        suffix: 'ms'
      },
      toolTip: {
        shared: true
      },
      data: data
    });
    this.chart.render();
  }

  getData() {
    let data = new Array(5);
    for (let i = 0; i < 5; ++i) {
      data[i] = {
        type: "column",
        name: i < 4 ? `O${i}` : 'GA Optimization',
      }
      data[i].dataPoints = this.getDataPoints(i);
    }
    return data;
  }

  getDataPoints(i) {
    let datapoints = new Array(4);
    for (let j = 0; j < 4; ++j) {
      datapoints[j] = {
        y: this.getExecTime(i, j) * 1000,
        label: this.pgmNames[j]
      }
    }
    return datapoints;
  }

  getExecTime(i, j) {
    switch (i) {
      case 0:
        return this.benchMarks[j].O0.exec_time
      case 1:
        return this.benchMarks[j].O1.exec_time
      case 2:
        return this.benchMarks[j].O2.exec_time
      case 3:
        return this.benchMarks[j].O3.exec_time
      case 4:
        return this.benchMarks[j].GAOpt.exec_time
    }
  }

}
