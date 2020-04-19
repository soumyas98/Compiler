import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MetaDataChartComponent } from './meta-data-chart.component';

describe('MetaDataChartComponent', () => {
  let component: MetaDataChartComponent;
  let fixture: ComponentFixture<MetaDataChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MetaDataChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MetaDataChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
