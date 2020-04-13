import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService, DataSet } from '../app.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {
  experimentName: string;
  datasets: DataSet[];
  selectedDataSet: DataSet;
  features: string;

  constructor(private appService: AppService, 
              private route: ActivatedRoute) { 
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      let id = +params.get('id');
      this.experimentName = this.appService.getExperimentName(id);
      this.datasets = this.appService.getDataSets(id);
      this.selectedDataSet = this.datasets[0];
    });
  }

  onChange(newValue: DataSet): void {
    this.selectedDataSet = newValue;
    console.log(this.selectedDataSet)
    this.features = this.selectedDataSet.toString()
  }

}