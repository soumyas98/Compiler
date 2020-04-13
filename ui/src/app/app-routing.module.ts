import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IndexComponent } from './index/index.component';
import { MainComponent } from './main/main.component';


const routes: Routes = [
  { path: 'home', component: IndexComponent },
  { path: 'experiment/:id', component: MainComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
