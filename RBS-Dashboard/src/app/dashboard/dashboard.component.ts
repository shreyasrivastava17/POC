import { Component, OnInit } from '@angular/core';
import { interval } from 'rxjs';
// import { Http, Response, RequestMethod, RequestOptions, Headers } from '@angular/http';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  result:any;
  customers:any=[["abd","yes"]]
  customer:any = []
  isValid: Boolean = true;
  constructor(private http: HttpClient) { }

  ngOnInit() {
    interval(2000 ).subscribe(x => {
      // this.customers.push("svc")
      this.http.get('http://127.0.0.1:5000/GetCustomerNames')
      .subscribe((res: any) => {
        this.customers=[]
        for(var i=0;i<res.length;i++)
        {
          console.log(res[i]['Name'])
          this.customer.push(res[i]['Name'])
          this.customer.push(res[i]['IsSignificant'])
          this.customers.push(this.customer)
          this.customer = []
          console.log(this.customers)
        }     
      }, error => {
        console.log(error);
       
      });
    });
  }

}
