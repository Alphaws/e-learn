import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BlogListComponent } from "@modules/blog/blog-list/blog-list.component";
import { BlogDetailsComponent } from "@modules/blog/blog-details/blog-details.component";

const routes: Routes = [
  {
    path: '',
    component: BlogListComponent
  },
  {
    path: ':slug',
    component: BlogDetailsComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BlogRoutingModule { }
