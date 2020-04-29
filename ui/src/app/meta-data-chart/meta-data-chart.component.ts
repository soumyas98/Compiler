import { Component, OnInit, Input } from '@angular/core';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-meta-data-chart',
  templateUrl: './meta-data-chart.component.html',
  styleUrls: ['./meta-data-chart.component.css']
})
export class MetaDataChartComponent implements OnInit {
  chart: any;
  mutationDataPoints: any[] = [];
  crossoverDataPoints: any[] = [];

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("metaDataChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Generation',
        interval: 1
      },
      axisY: {
        title: 'Count',
        minimum: 0
      },
      toolTip: {
        shared: true
      },
      legend: {
        cursor: "pointer",
        verticalAlign: "top",
        horizontalAlign: "right",
        dockInsidePlotArea: false,
      },
      data: [{
        type: "column",
        color: "teal",
        name: "Mutation",
        showInLegend: true,
        dataPoints: this.mutationDataPoints
      }, {
        type: "column",
        color: "wheat",
        name: "Crossover",
        showInLegend: true,
        dataPoints: this.crossoverDataPoints
      }]
    });
    this.chart.render();
  }

  updateChart(currGenIdx, prevMutationCount, prevCrossoverCount): void {
    if (currGenIdx > this.mutationDataPoints.length) {
      this.mutationDataPoints.push({
        x: this.mutationDataPoints.length,
        y: prevMutationCount
      });
      this.crossoverDataPoints.push({
        x: this.crossoverDataPoints.length,
        y: prevCrossoverCount
      });
    }
    this.chart.render();
  }

  reset(): void {
    this.mutationDataPoints.length = 0;
    this.crossoverDataPoints.length = 0;
    this.chart.render();
  }

}
