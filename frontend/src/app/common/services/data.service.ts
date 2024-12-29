import { inject, Injectable } from '@angular/core';
import { HttpClient, HttpContext } from "@angular/common/http";
import { environment } from "@environments/environment";
import { IS_PUBLIC } from "@interceptors/jwt.interceptor";

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http = inject(HttpClient);
  apiUrl = environment.apiUrl;
  private readonly CONTEXT = {context: new HttpContext().set(IS_PUBLIC, true)};

  constructor() { }

  getSubjects() {
    return this.http.get(`${this.apiUrl}/api/subjects/`, this.CONTEXT);
    // this.apiUrl + '/api/subjects/'
  }

  getSubject(slug: string) {
    return this.http.get(this.apiUrl + '/api/subject/' + slug + '/', this.CONTEXT);
  }
}
