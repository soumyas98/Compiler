import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MemberChartComponent } from './member-chart.component';

describe('MemberChartComponent', () => {
  let component: MemberChartComponent;
  let fixture: ComponentFixture<MemberChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MemberChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MemberChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
