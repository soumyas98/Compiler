import { Component, OnInit } from '@angular/core';
import { AppService, DataSet } from '../app.service';
import { GA } from '../model/GA';

@Component({
  selector: 'app-conclusion',
  templateUrl: './conclusion.component.html',
  styleUrls: ['./conclusion.component.css']
})
export class ConclusionComponent implements OnInit {
  benchMarks: any[] = new Array(4);

  constructor(private appService: AppService) { 
    this.benchMarks[0] = { name: 'Basic Math', benchMark: null }
    this.benchMarks[1] = { name: 'Bit Count', benchMark: null }
    this.benchMarks[2] = { name: 'Quick Sort', benchMark: null }
    this.benchMarks[3] = { name: 'Susan Image Processing', benchMark: null }
  }

  ngOnInit() {
    for (let i = 0; i < 1; ++i) {
      this.appService.getData(i + 1, DataSet.SMALL).subscribe(data => {
        this.benchMarks[i].benchMark = (new GA(data)).benchmark;
        console.log('Bench mark', this.benchMarks[i].benchMark);
      });
    }
  }

}
