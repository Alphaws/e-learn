import { Routes } from '@angular/router';
import { HomeComponent } from "./modules/home/home/home.component";

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 's/:slug',
    component: HomeComponent
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];
