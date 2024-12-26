import { inject, Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class DataService {
  http = inject(HttpClient);

  constructor() { }

  getData() {
    return this.http.get('data/subjects.json');

  }
}
