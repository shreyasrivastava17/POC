import { Component, OnInit } from '@angular/core';
import { MediaMatcher } from '@angular/cdk/layout';
import { ChangeDetectorRef, OnDestroy } from '@angular/core';


@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit, OnDestroy {
  mobileQuery: MediaQueryList;
  resourceload:any;
  private _mobileQueryListner: () => void;
  element: HTMLElement ;
  constructor( changeDetectorRef: ChangeDetectorRef, media: MediaMatcher) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListner = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListner);
   }

  ngOnInit() {

  }
  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListner);

  }
  toggleActive(event:any){
    debugger;
    event.preventDefault();
    if(this.element !== undefined){
      this.element.style.backgroundColor = "white";
    } 
    var target = event.currentTarget;
    target.style.backgroundColor = "#007DC3";
    this.element = target;
  }
  // switchHome(){
  //   //debugger;
  //   if(this.data.flag == true){
  //     this.data.isAuthenticated();
  //   }
  // }

}
