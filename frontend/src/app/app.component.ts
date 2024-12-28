import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from "./common/layout/navbar/navbar.component";
import { FooterComponent } from "./common/layout/footer/footer.component";
import { initFlowbite } from "flowbite";
import { TranslateService } from "@ngx-translate/core";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NavbarComponent, FooterComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {

  title = 'frontend';

  constructor(private translate: TranslateService) {
    this.translate.addLangs(['hu', 'en', 'de']);
    this.translate.setDefaultLang('en');
    this.translate.use('en');
  }


  ngOnInit() {
    initFlowbite()
  }
}
