import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FitnessChartComponent } from './fitness-chart.component';

describe('FitnessChartComponent', () => {
  let component: FitnessChartComponent;
  let fixture: ComponentFixture<FitnessChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FitnessChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FitnessChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
