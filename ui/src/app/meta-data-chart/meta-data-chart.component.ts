import { Component, OnInit, Input } from '@angular/core';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-meta-data-chart',
  templateUrl: './meta-data-chart.component.html',
  styleUrls: ['./meta-data-chart.component.css']
})
export class MetaDataChartComponent implements OnInit {
  @Input() data: GA;
  chart: any;
  execDataPoints: any[] = [];
  compDataPoints: any[] = [];

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("metaDataChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Member',
        minimum: 0,
        maximum: this.data.population * this.data.generation_count
      },
      axisY: {
        title: 'Time',
        minimum: 0,
        maximum: Math.ceil(Math.max(this.data.max_exec_time, this.data.max_comp_time)) * 1000,
        suffix: 'ms'
      },
      toolTip: {
        shared: true
      },
      legend: {
        cursor: "pointer",
        verticalAlign: "top",
        horizontalAlign: "right",
        dockInsidePlotArea: true,
      },
      data: [{
        type: "line",
        color: "teal",
        name: "Execution Time",
        showInLegend: true,
        dataPoints: this.execDataPoints
      }, {
        type: "line",
        color: "wheat",
        name: "Compile Time",
        showInLegend: true,
        dataPoints: this.compDataPoints
      }]
    });
    this.chart.render();
  }

  updateChart(): void {
    let execTime = this.data.getCurrentMemberExecTime();
    let compTime = this.data.getCurrentMemberCompTime();
    if (!execTime) {
      return;
    }
    this.execDataPoints.push({
      x: this.execDataPoints.length,
      y: execTime * 1000
    });
    this.compDataPoints.push({
      x: this.compDataPoints.length,
      y: compTime * 1000
    });
    if (this.chart) {
      this.chart.render();
    }
  }

  reset(): void {
    this.execDataPoints.length = 0;
    this.compDataPoints.length = 0;
    if (this.chart) {
      this.chart.render();
    }
  }

}
