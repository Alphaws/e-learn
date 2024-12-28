import { inject, Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { environment } from "@environments/environment";

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http = inject(HttpClient);
  apiUrl = environment.apiUrl;

  constructor() { }

  getSubjects() {
    return this.http.get(this.apiUrl + 'api/subjects/');
  }

  getSubject(slug: string) {
    return this.http.get(this.apiUrl + 'api/subject/' + slug + '/');
  }
}
