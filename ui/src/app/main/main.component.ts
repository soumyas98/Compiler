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
  selectedIdx: Number;

  constructor(private appService: AppService, 
              private route: ActivatedRoute) { 
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.selectedIdx = -1;
      let id = +params.get('id');
      this.experimentName = this.appService.getExperimentName(id);
      this.datasets = this.appService.getDataSets(id);
    });
  }

  select(i: Number): void {
    this.selectedIdx = i;
  }

}