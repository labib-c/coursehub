import { Component, Input } from '@angular/core';
import { CourseCardDataService } from "./course-card-data.service";
import { Router } from '@angular/router';

@Component({
  selector: 'app-course-card',
  templateUrl: './course-card.component.html',
  styleUrls: ['./course-card.component.scss'],
})

export class CourseCardComponent {
  @Input() name : string = '';
  @Input() description: string;
  @Input() color: String;
  @Input() percentColor: String;
  @Input() totalRating: number;

  textbooks: String[];
  difficultyRating: number;
  usefulnessRating: number;

  constructor(private courseCardDataService: CourseCardDataService, private _router: Router) {
    this.color = 'blue';
    this.percentColor='orange';
  }

  navigateToCoursePage() {
    this._router.navigate(['/course-page']);
    this.courseCardDataService.populateCourseCardData(this.name, this.description, this.totalRating);
  }
}
