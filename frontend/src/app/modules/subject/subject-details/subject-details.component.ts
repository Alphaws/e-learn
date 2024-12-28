import { Component, inject, OnInit } from '@angular/core';
import { ActivatedRoute } from "@angular/router";
import { DataService } from "@services/data.service";
import { JsonPipe } from "@angular/common";
import { LanguageService } from "@services/language.service";

@Component({
  selector: 'app-subject-details',
  imports: [],
  templateUrl: './subject-details.component.html',
  styleUrl: './subject-details.component.scss'
})
export class SubjectDetailsComponent implements OnInit {

  languageService: any = inject(LanguageService);
  language$ = this.languageService.language;  // A Signal változó


  id = '';
  subject : any = null;

  constructor(
      public activatedRoute: ActivatedRoute,
      private dataService: DataService
  ) {}

  ngOnInit() {
    this.activatedRoute.paramMap.subscribe((params) => {
      this.id = params.get('slug') || '';
      this.dataService.getSubject(this.id).subscribe({
        next: (response: any) => {
          this.subject = response
        },
        error: (err: any) => {
          console.log(err);
        }
      });
    });
  }

}
