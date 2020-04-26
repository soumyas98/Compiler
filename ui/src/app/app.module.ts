import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { HeaderComponent } from './header/header.component';
import { NavbarComponent } from './navbar/navbar.component';
import { FooterComponent } from './footer/footer.component';
import { MainComponent } from './main/main.component';
import { IndexComponent } from './index/index.component';
import { ExperimentComponent } from './experiment/experiment.component';
import { MemberChartComponent } from './member-chart/member-chart.component';
import { MetaDataChartComponent } from './meta-data-chart/meta-data-chart.component';
import { FitnessChartComponent } from './fitness-chart/fitness-chart.component';
import { BenchmarkChartComponent } from './benchmark-chart/benchmark-chart.component';
import { ConclusionComponent } from './conclusion/conclusion.component';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    NavbarComponent,
    FooterComponent,
    MainComponent,
    IndexComponent,
    ExperimentComponent,
    MemberChartComponent,
    MetaDataChartComponent,
    FitnessChartComponent,
    BenchmarkChartComponent,
    ConclusionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
