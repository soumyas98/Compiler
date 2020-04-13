import { Component, OnInit } from '@angular/core';
import { AppService } from '../app.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  links:any[];

  constructor(private appSerivce:AppService) { 
    this.links = [
      { title: "Home", path: "/home"},
      { title: this.appSerivce.getExperimentName(1), path: "/experiment/1"},
      { title: this.appSerivce.getExperimentName(2), path: "/experiment/2"},
      { title: this.appSerivce.getExperimentName(3), path: "/experiment/3"},
      { title: this.appSerivce.getExperimentName(4), path: "/experiment/4"},
      { title: "Conclusion", path: "/index"},
    ]
  }

  ngOnInit() {
  }

}
