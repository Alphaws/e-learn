import { Component, inject, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavbarComponent } from "./common/layout/navbar/navbar.component";
import { FooterComponent } from "./common/layout/footer/footer.component";
import { initFlowbite } from "flowbite";
import { TranslateService } from "@ngx-translate/core";
import { AuthService } from "@services/auth.service";
import { environment } from "@environments/environment";

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, NavbarComponent, FooterComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {

  user: any = null;
  title = environment.title;
  authService: any = inject(AuthService);

  constructor(private translate: TranslateService) {
    this.translate.addLangs(['hu', 'en', 'de']);
    this.translate.setDefaultLang('en');
    this.translate.use('en');
  }


  ngOnInit() {
    initFlowbite();
    this.authService.getProfileData().subscribe({
      next: (data: any) => {
        console.log(data);
        this.user = data; // Felhasználó adatai
      },
      error: (err: any) => {
        console.error(err);
        this.user = null; // Hibakezelés, pl. ha nem bejelentkezett
      },
    });
  }
}
