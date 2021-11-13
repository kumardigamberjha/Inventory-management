from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('user-status/', views.user_status, name="user-status"),
    path('IT-Purchase/', views.Purchase_Item, name="IT-Purchase"),
    path('User-requisition/', views.User_requisition, name="user-requisition"),

    path('user-values/<id>/', views.user_value, name="user-value"),
    path('Issued-items/', views.Issued_To, name="issued"),
    path('show-all-status/', views.Opening_Stocks, name="show-all-items"),
    path("SignUp/", views.Signup_view, name="signup"),
    path('login/', views.Login_view, name="login"),
    path('logout/', views.Logout_view, name="logout"),
    path('purchase_form/<req_number>/', views.Purchase_Form, name="IT-form"),
    path('opening_stock_form/', views.Opening_Stock_FormView, name="opening_stock_form"),
    path('requisition-form/', views.User_requisition_form, name="requistion-form"),
    path('receiving-form/<purchase_id>', views.Receiving_Item_Form, name="receiving-form"),
    path('All_Purchase/', views.All_Purchased_Item, name="all_purchase"),
    path('Purchase_Issue_Item_form/<purchase_id>', views.Purchase_Issue_Form, name="purchase_issue_form"),
    path('Stock_Issue_Item_form/<stock_id>', views.Stock_Issue_Form, name="stock_issue_form"),
    path('total_stock/', views.Total_Stock, name="total_stock"),

    # MASTER DATA
    path('user-master/', views.User_Master_Admin, name="user_master_admin"),
    path("add_user_master/", views.Add_User, name="add_user_master"),
    path("edit_user_master/<int:id>/", views.Edit_User_Form, name="edit_user_master"),
    path("delete_user_master/<int:id>/", views.Delete_User, name="delete_user_master"),

    # Item Master Data
    path("add_item_master/", views.Add_Item_Form, name="add_item_master"),
    path("edit_item_master/<int:id>/", views.Edit_Item_Form, name="edit_item_master"),
    path("delete_item_master/<int:id>/", views.Delete_Item, name="delete_item_master"),

    # Vendor Master Data
    path("add_vendor_master/", views.Add_Vendor_Form, name="add_vendor_master"),
    path("edit_vendor_master/<int:id>/", views.Edit_Vendor_Form, name="edit_vendor_master"),
    path("delete_vendor_master/<int:id>/", views.Delete_Vendor, name="delete_vendor_master"),
    
    # Brand Master Data
    path("add_brand_master/", views.Add_Brand_Form, name="add_brand_master"),
    path("edit_brand_master/<int:id>/", views.Edit_Brand_Form, name="edit_brand_master"),
    path("delete_department_master/<int:id>/", views.Delete_Brand, name="delete_brand_master"),
      
   # Department Master Data
    path("add_department_master/", views.Add_Department_Form, name="add_department_master"),
    path("edit_department_master/<int:id>/", views.Edit_Department_Form, name="edit_department_master"),
    path("delete_department_master/<int:id>/", views.Delete_Department, name="delete_department_master"),
   
    # path('Trace_order/', views.Order_trace, name="trace-order"),
    # path('Update_form/<req_number>/', views.Edit_User_Requisition, name="update-user-requisition-form"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)