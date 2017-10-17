# Sublime Text 3 OneLineCopy

Sublime plugin which allows copying multiple lines to the clipboard as one line
by removing lines breaks and redundant spaces. Useful for quickly copying and 
pasting small blocks of Ruby code into the Rails console.

```ruby
thing.each do |thing|
  thing.foo
end
```

becomes

```ruby
thing.each do |thing| thing.foo end
```

## Usage

Clone the repository and copy the folder into your Sublime `Packages/` directory.
Use `Super+Shift+C` (for Linux and Windows respectively `Ctrl+Shift+C`) to copy
the selection as one line. 
