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
    path: 'p',
    loadChildren: () =>
        import('./modules/project/project.module').then(m => m.ProjectModule),
  },
  {
    path: 'c',
    loadChildren: () =>
        import('./modules/course/course.module').then(m => m.CourseModule),
  },
  {
    path: 'b',
    loadChildren: () =>
        import('./modules/blog/blog.module').then(m => m.BlogModule),
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];
