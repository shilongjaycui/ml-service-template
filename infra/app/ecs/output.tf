output "alb_dns_name" {
  value = "http://${aws_lb.this.dns_name}/docs"
}