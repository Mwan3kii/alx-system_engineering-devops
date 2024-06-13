exec { 'increase-buffers':
  command => 'sed -i "s/# server_names_hash_bucket_size .*/server_names_hash_bucket_size 64;/" /etc/nginx/nginx.conf && sed -i "s/keepalive_timeout .*/keepalive_timeout 65;/" /etc/nginx/nginx.conf && systemctl restart nginx',
}
