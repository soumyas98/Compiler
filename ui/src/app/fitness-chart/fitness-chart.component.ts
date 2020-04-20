import { Component, OnInit, Input } from '@angular/core';
import { GA } from '../model/GA';
import * as CanvasJS from '../canvasjs-2.3.2/canvasjs.min';

@Component({
  selector: 'app-fitness-chart',
  templateUrl: './fitness-chart.component.html',
  styleUrls: ['./fitness-chart.component.css']
})
export class FitnessChartComponent implements OnInit {
  @Input() data: GA;
  chart: any;
  averageFitnessDataPoints: any[] = [];
  bestFitnessDataPoints: any[] = [];

  constructor() { }

  ngOnInit() {
    this.initChart();
  }

  initChart(): void {
    this.chart = new CanvasJS.Chart("fitnessChartContainer", {
      animationEnabled: true,
      axisX: {
        title: 'Generation',
        minimum: 0,
        maximum: this.data.generation_count
      },
      axisY: {
        title: 'Fitness',
        minimum: 0,
        maximum: (1 / this.data.generations[this.data.generation_count - 1].fittest.exec_time) + 0.5
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
        name: "Average fitness",
        showInLegend: true,
        dataPoints: this.averageFitnessDataPoints
      }, {
        type: "line",
        color: "wheat",
        name: "Best fitness",
        showInLegend: true,
        dataPoints: this.bestFitnessDataPoints
      }]
    });
    this.chart.render();
  }

  updateChart(): void {
    if (this.data.getCurrentGenerationIdx() > this.averageFitnessDataPoints.length) {
      this.averageFitnessDataPoints.push({
        x: this.averageFitnessDataPoints.length,
        y: this.data.getPreviousGen('AVG_FIT')
      });
      this.bestFitnessDataPoints.push({
        x: this.bestFitnessDataPoints.length,
        y: 1 / this.data.getPreviousGen('FITTEST_EXEC')
      });
    }
    this.chart.render();
  }

  reset(): void {
    this.averageFitnessDataPoints.length = 0;
    this.bestFitnessDataPoints.length = 0;
    this.chart.render();
  }

}
