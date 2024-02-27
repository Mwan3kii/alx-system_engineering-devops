#!/usr/bin/env ruby
entry = ARGV[0]
sender_regex = /\[from:([^ \]]+)\]/
receiver_regex = /\[to:([^ \]]+)\]/
flags_regex = /\[flags:([^ \]]+)\]/
sender = entry.match(sender_regex)[1]
receiver = entry.match(receiver_regex)[1]
flags = entry.match(flags_regex)[1]
puts "#{sender},#{receiver},#{flags}"
