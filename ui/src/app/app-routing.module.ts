import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { MainComponent } from './main/main.component';
import { ExperimentComponent } from './experiment/experiment.component';
import { ConclusionComponent } from './conclusion/conclusion.component';


const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: IndexComponent },
  { 
    path: 'experiment/:id',
    component: MainComponent,
    children: [
      { path: ':dataset', component: ExperimentComponent }
    ]
  },
  {
    path: 'conclusion',
    component: ConclusionComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
