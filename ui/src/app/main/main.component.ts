import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AppService } from '../app.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {
  experimentName:string;

  constructor(private appService: AppService, 
              private route: ActivatedRoute) { 
  }

  ngOnInit() {
    this.route.paramMap.subscribe(params => {
      this.experimentName = this.appService.getExperimentName(+params.get('id'));
    });
  }

  getExperimentTitle(id:Number):string {
    switch (id) {
      case 1:
        return "Basic Math"
    }
    return null; 
  }

}
