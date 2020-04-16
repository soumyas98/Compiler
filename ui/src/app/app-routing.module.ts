import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { MainComponent } from './main/main.component';
import { ExperimentComponent } from './experiment/experiment.component';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: IndexComponent },
  { 
    path: 'experiment/:id',
    component: MainComponent,
    children: [
      { path: ':dataset', component: ExperimentComponent }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
