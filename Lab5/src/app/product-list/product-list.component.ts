import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product, products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  
  products: Product[] = [];
  productCategoryFromRoute!: string;
  currentImageIndex = 0;

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    this.productCategoryFromRoute = String(routeParams.get('productCategory')).toLowerCase();
  
    // Find all products that correspond with the category provided in route.
    this.products = products.filter(product => {
      const match = product.category.toLowerCase() === this.productCategoryFromRoute;
      if (!match) {
        console.log('Mismatching product:', product);
      }
      return match;
    });
  }

  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }

  getWhatsAppShareLink(productId: number) {
    return `https://api.whatsapp.com/send?text=${encodeURIComponent(this.products[productId - 1].href)}`;
  } 

  getTelegramShareLink(productId: number) {
    return `https://t.me/share/url?url=${encodeURIComponent(this.products[productId - 1].href)}`;
  }

  prevImage(productId: any) {
    this.currentImageIndex = Math.max(this.currentImageIndex - 1, 0);
  }

  nextImage(product: any) {
    this.currentImageIndex = Math.min(this.currentImageIndex + 1, product.img.length - 1);
  }
}
