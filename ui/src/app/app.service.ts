import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export enum DataSet {
  SMALL = "Small",
  LARGE = "Large"
}

@Injectable({
  providedIn: 'root'
})
export class AppService {
  ROOT_URL: string = 'assets/data/';

  constructor(private http: HttpClient) { }

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
        return [ DataSet.SMALL ];
    }
  }

  getData(id:Number, dataset: DataSet) {
    let url = this.ROOT_URL + id + '/' + dataset.toLowerCase() + '.json';
    return this.http.get(url);
  }

  getFeatureData(id:Number) {
    let url = this.ROOT_URL + id + '/' + 'feature.json';
    return this.http.get(url);
  }

  getInterval() {
    return 50;
  }

}
