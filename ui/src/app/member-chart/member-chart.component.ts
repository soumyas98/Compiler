import { Component, OnInit, Input, ChangeDetectorRef } from '@angular/core';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-member-chart',
  templateUrl: './member-chart.component.html',
  styleUrls: ['./member-chart.component.css']
})
export class MemberChartComponent implements OnInit {
  chart: any;
  execDataPoints: any[] = [];
  compDataPoints: any[] = [];

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("memberChartContainer", {
      animationEnabled: true,
      zoomEnabled: true,
      axisX: {
        title: 'Member',
        minimum: 0
      },
      axisY: {
        title: 'Time',
        minimum: 0,
        suffix: 's'
      },
      toolTip: {
        shared: true
      },
      legend: {
        cursor: "pointer",
        verticalAlign: "top",
        horizontalAlign: "right",
        itemclick: this.toggleDataSeries,
        dockInsidePlotArea: false
      },
      data: [{
        type: "scatter",
        color: "teal",
        name: "Execution Time",
        markerSize: 3,
        showInLegend: true,
        dataPoints: this.execDataPoints
      }, {
        type: "scatter",
        color: "wheat",
        name: "Compile Time",
        markerSize: 3,
        showInLegend: true,
        dataPoints: this.compDataPoints
      }]
    });
    this.chart.render();
  }

  updateChart(execTime: number, compTime: number): void {
    if (!execTime) {
      return;
    }
    this.execDataPoints.push({
      x: this.execDataPoints.length,
      y: execTime
    });
    this.compDataPoints.push({
      x: this.compDataPoints.length,
      y: compTime
    });
    this.chart.render();
  }

  reset(): void {
    this.execDataPoints.length = 0;
    this.compDataPoints.length = 0;
    this.chart.render();
  }

  toggleDataSeries(e) {
    if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
      e.dataSeries.visible = false;
    } else {
      e.dataSeries.visible = true;
    }
    e.chart.render();
  }

}
