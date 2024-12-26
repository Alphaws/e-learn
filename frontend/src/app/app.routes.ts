import { Routes } from '@angular/router';
import { HomeComponent } from "./modules/home/home/home.component";
import { SubjectDetailsComponent } from "./modules/subject/subject-details/subject-details.component";

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
    component: SubjectDetailsComponent
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];
