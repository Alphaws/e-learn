import { Component, inject, OnInit } from '@angular/core';
import { NgForOf } from "@angular/common";
import { RouterLink } from "@angular/router";
import { DataService } from "../../../common/services/data.service";


@Component({
  selector: 'app-home',
  imports: [
    NgForOf,
    RouterLink
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {

  dataService: any = inject(DataService);
  subjects: any[] = [];

  constructor() {}

  ngOnInit() {
    this.dataService.getData().subscribe({
      next: (data: any) => {
        this.subjects = data;
        console.log(this.subjects);
      },
      error: (err: any) => {
        console.log(err);
      }
    })
  }
}
