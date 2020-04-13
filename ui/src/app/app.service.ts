import { Injectable } from '@angular/core';

export enum DataSet {
  SMALL = "Small",
  LARGE = "Large"
}

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor() { }

  getExperimentName(id:Number): string {
    switch (id) {
      case 1:
        return 'Basic Math';
      case 2:
        return 'Bit Count';
      case 3:
        return 'Quick Sort';
      case 4:
        return 'Susan Image Processing';
    }
  }

  getDataSets(id:Number): DataSet[] {
    switch (id) {
      case 1:
        return [ DataSet.SMALL, DataSet.LARGE];
      case 2:
        return [ DataSet.SMALL, DataSet.LARGE];
      case 3:
        return [ DataSet.SMALL, DataSet.LARGE];
      case 4:
        return [ DataSet.SMALL, DataSet.LARGE];
    }
  }

}
