import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor() { }

  getExperimentName(id:Number) {
    switch (id) {
      case 1:
        return "Basic Math";
      case 2:
        return "Bit Count";
      case 3:
        return "Quick Sort";
      case 4:
        return "Susan Image Processing";
    }
  }
}
