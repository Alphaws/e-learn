import { inject, Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { environment } from "@environments/environment";

@Injectable({
  providedIn: 'root'
})
export class BlogService {

  http = inject(HttpClient);
  apiUrl = environment.apiUrl;

  constructor() { }

  getBlogPostsForSubject(subjectSlug: string) {
    return this.http.get(this.apiUrl + 'api/blog/' + subjectSlug + '/');
  }
}
