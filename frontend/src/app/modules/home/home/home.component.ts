import { Component, inject, OnInit } from '@angular/core';
import { NgForOf } from "@angular/common";
import { RouterLink } from "@angular/router";
import { DataService } from "../../../common/services/data.service";
import { TranslatePipe } from "@ngx-translate/core";
import { LanguageService } from "../../../common/services/language.service";
import { SubjectInterface } from "@interfaces/subject.interface";


@Component({
  selector: 'app-home',
  imports: [
    NgForOf,
    RouterLink,
    TranslatePipe
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent implements OnInit {

  dataService: any = inject(DataService);
  languageService: any = inject(LanguageService);
  subjects: SubjectInterface[] = [];
  language$ = this.languageService.language;  // A Signal változó


  constructor() {}

  ngOnInit() {
    this.dataService.getSubjects().subscribe({
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
