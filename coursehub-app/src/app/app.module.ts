import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { WavesModule, CardsFreeModule } from 'angular-bootstrap-md'
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { FormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { AuthInterceptor } from './auth/auth.interceptor';
import { DashboardComponent } from './views/dashboard/dashboard.component';
import { CourseCardComponent } from './components/course-card/course-card.component';
import { SearchbarComponent } from './components/searchbar/searchbar.component';
import { AppRoutingModule } from './app-routing.module';
import { CoursePageComponent } from './views/course-page/course-page.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { CommentComponent } from  './components/comment/comment.component';
import { ReadMoreComponent } from './components/read-more/read-more.component';
import { CommentDataService } from './components/comment/comment-data.service';
import { SearchbarService } from './components/searchbar/searchbar.service';
import { CourseCardDataService } from './components/course-card/course-card-data.service';
import { CoursePageDataService } from './views/course-page/course-page-data.service';
import { AuthService } from './auth/auth.service';
import { LoadingComponent } from './components/loading/loading.component';
import { NavbarComponent } from './components/navbar/navbar.component';

import { AppComponent } from './app.component';
import { ProfileComponent } from './views/profile/profile.component';


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    CourseCardComponent,
    SearchbarComponent,
    CoursePageComponent,
    SidebarComponent,
    CommentComponent,
    ReadMoreComponent,
    LoadingComponent,
    NavbarComponent,
    ProfileComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    WavesModule,
    CardsFreeModule,
    HttpClientModule,
    MDBBootstrapModule.forRoot(),
    FormsModule,
    AppRoutingModule,
  ],
  providers: [
    SearchbarService, 
    CourseCardDataService, 
    CoursePageDataService, 
    CommentDataService,
    AuthService,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }
