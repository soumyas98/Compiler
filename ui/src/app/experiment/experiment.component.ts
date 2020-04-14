import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService, DataSet } from '../app.service';

@Component({
  selector: 'app-experiment',
  templateUrl: './experiment.component.html',
  styleUrls: ['./experiment.component.css']
})
export class ExperimentComponent implements OnInit {
  id: Number;
  dataset: DataSet;
  data: any;

  constructor(private appSerivce: AppService, private route: ActivatedRoute) { }

  ngOnInit() {
    this.id = +this.route.parent.snapshot.paramMap.get('id');
    this.route.paramMap.subscribe(params => {
      this.dataset = DataSet[params.get('dataset').toUpperCase()];
      console.log(this.id, this.dataset);
      this.updateComponent();
    });
  }

  updateComponent(): void {
    this.appSerivce.getData(this.id, this.dataset).subscribe(data => {
      this.data = data;
      console.log(this.data);
    });
  }

}
