# Binary Data Manipulation in Go

This comprehensive guide contains 80 detailed Go code examples demonstrating working with binary data. Each example showcases practical use cases, best practices, and educational concepts for binary data manipulation in Go.

## Table of Contents

1. [Basic Byte Operations and Byte Slices (1-10)](#basic-byte-operations-and-byte-slices)
2. [Reading and Writing Binary Files (11-20)](#reading-and-writing-binary-files)
3. [Bitwise Operations and Bit Manipulation (21-30)](#bitwise-operations-and-bit-manipulation)
4. [Encoding and Decoding (31-40)](#encoding-and-decoding)
5. [Buffer Operations and Management (41-50)](#buffer-operations-and-management)
6. [Endianness Handling (51-60)](#endianness-handling)
7. [Advanced Binary Manipulation (61-70)](#advanced-binary-manipulation)
8. [Real-world Binary Data Scenarios (71-80)](#real-world-binary-data-scenarios)

---

## Basic Byte Operations and Byte Slices

### Example 1: Creating and Working with Byte Slices

```go
package main

import (
    "fmt"
)

func main() {
    // Creating byte slices in different ways
    
    // Method 1: Using byte literal
    data1 := []byte("Hello, World!")
    fmt.Printf("Method 1: %v\n", data1)
    fmt.Printf("As string: %s\n", string(data1))
    
    // Method 2: Using make with specified capacity
    data2 := make([]byte, 5, 10) // length 5, capacity 10
    copy(data2, []byte("Golan"))
    fmt.Printf("Method 2: %v\n", data2)
    
    // Method 3: Creating from hex values
    data3 := []byte{0x48, 0x65, 0x6C, 0x6C, 0x6F} // "Hello"
    fmt.Printf("Method 3: %v -> %s\n", data3, string(data3))
    
    // Method 4: Using append to build incrementally
    var data4 []byte
    data4 = append(data4, 'G', 'o')
    data4 = append(data4, []byte(" rocks!")...)
    fmt.Printf("Method 4: %s\n", string(data4))
}
```

### Example 2: Byte Slice Manipulation and Copying

```go
package main

import (
    "fmt"
)

func main() {
    original := []byte("Original Data")
    fmt.Printf("Original: %s\n", string(original))
    
    // Shallow copy vs deep copy
    shallow := original // shares underlying array
    deep := make([]byte, len(original))
    copy(deep, original) // creates new underlying array
    
    // Modify original
    original[0] = 'M'
    
    fmt.Printf("After modifying original[0]:\n")
    fmt.Printf("Original: %s\n", string(original))
    fmt.Printf("Shallow:  %s\n", string(shallow))  // Changed!
    fmt.Printf("Deep:     %s\n", string(deep))     // Unchanged
    
    // Slicing operations
    data := []byte("Hello, World!")
    slice1 := data[0:5]    // "Hello"
    slice2 := data[7:]     // "World!"
    slice3 := data[:]      // Full slice
    
    fmt.Printf("\nSlicing operations:\n")
    fmt.Printf("slice1: %s\n", string(slice1))
    fmt.Printf("slice2: %s\n", string(slice2))
    fmt.Printf("slice3: %s\n", string(slice3))
    
    // Capacity and length
    fmt.Printf("\nCapacity and length info:\n")
    fmt.Printf("len(data): %d, cap(data): %d\n", len(data), cap(data))
    fmt.Printf("len(slice1): %d, cap(slice1): %d\n", len(slice1), cap(slice1))
}
```

### Example 3: Converting Between Types and Byte Slices

```go
package main

import (
    "fmt"
    "strconv"
    "unsafe"
)

func main() {
    // String to []byte and back
    str := "Hello, 世界"
    byteSlice := []byte(str)
    backToString := string(byteSlice)
    
    fmt.Printf("Original string: %s\n", str)
    fmt.Printf("As byte slice: %v\n", byteSlice)
    fmt.Printf("Back to string: %s\n", backToString)
    
    // Integer to bytes (manual conversion)
    num := 1234567890
    numStr := strconv.Itoa(num)
    numBytes := []byte(numStr)
    fmt.Printf("Number %d as bytes: %v\n", num, numBytes)
    
    // Using unsafe for zero-copy string to []byte conversion
    // WARNING: This is unsafe and should be used carefully
    unsafeBytes := (*[1 << 30]byte)(unsafe.Pointer(unsafe.StringData(str)))[:len(str):len(str)]
    fmt.Printf("Unsafe conversion: %v\n", unsafeBytes)
    
    // Rune to bytes
    r := '世'
    runeBytes := make([]byte, 4)
    n := copy(runeBytes, string(r))
    fmt.Printf("Rune '世' as bytes: %v (used %d bytes)\n", runeBytes[:n], n)
    
    // Boolean to byte
    boolTrue := byte(1)
    boolFalse := byte(0)
    fmt.Printf("Boolean true as byte: %d\n", boolTrue)
    fmt.Printf("Boolean false as byte: %d\n", boolFalse)
}
```

### Example 4: Byte Slice Search and Comparison

```go
package main

import (
    "bytes"
    "fmt"
)

func main() {
    data := []byte("The quick brown fox jumps over the lazy dog")
    pattern := []byte("fox")
    
    // Finding patterns
    index := bytes.Index(data, pattern)
    fmt.Printf("Pattern '%s' found at index: %d\n", string(pattern), index)
    
    // Finding last occurrence
    lastIndex := bytes.LastIndex(data, []byte("the"))
    fmt.Printf("Last 'the' found at index: %d\n", lastIndex)
    
    // Contains check
    contains := bytes.Contains(data, []byte("quick"))
    fmt.Printf("Contains 'quick': %t\n", contains)
    
    // Count occurrences
    count := bytes.Count(data, []byte("o"))
    fmt.Printf("Letter 'o' appears %d times\n", count)
    
    // Compare byte slices
    slice1 := []byte("apple")
    slice2 := []byte("banana")
    slice3 := []byte("apple")
    
    fmt.Printf("\nComparisons:\n")
    fmt.Printf("bytes.Compare(apple, banana): %d\n", bytes.Compare(slice1, slice2))
    fmt.Printf("bytes.Compare(apple, apple): %d\n", bytes.Compare(slice1, slice3))
    fmt.Printf("bytes.Equal(apple, apple): %t\n", bytes.Equal(slice1, slice3))
    
    // Case-insensitive operations
    upper := []byte("HELLO")
    lower := []byte("hello")
    fmt.Printf("Case-insensitive equal: %t\n", bytes.EqualFold(upper, lower))
}
```

### Example 5: Byte Slice Modification and Transformation

```go
package main

import (
    "bytes"
    "fmt"
)

func main() {
    data := []byte("  Hello, World!  ")
    fmt.Printf("Original: '%s'\n", string(data))
    
    // Trimming operations
    trimmed := bytes.TrimSpace(data)
    fmt.Printf("TrimSpace: '%s'\n", string(trimmed))
    
    trimPrefix := bytes.TrimPrefix(data, []byte("  "))
    fmt.Printf("TrimPrefix '  ': '%s'\n", string(trimPrefix))
    
    trimSuffix := bytes.TrimSuffix(data, []byte("  "))
    fmt.Printf("TrimSuffix '  ': '%s'\n", string(trimSuffix))
    
    // Splitting
    text := []byte("apple,banana,cherry,date")
    parts := bytes.Split(text, []byte(","))
    fmt.Printf("Split by comma: %v\n", parts)
    for i, part := range parts {
        fmt.Printf("  Part %d: %s\n", i, string(part))
    }
    
    // Joining
    words := [][]byte{
        []byte("Go"),
        []byte("is"),
        []byte("awesome"),
    }
    joined := bytes.Join(words, []byte(" "))
    fmt.Printf("Joined: %s\n", string(joined))
    
    // Replacing
    original := []byte("Hello World Hello Universe")
    replaced := bytes.Replace(original, []byte("Hello"), []byte("Hi"), -1)
    fmt.Printf("Replace all 'Hello' with 'Hi': %s\n", string(replaced))
    
    // Replace only first occurrence
    replaceFirst := bytes.Replace(original, []byte("Hello"), []byte("Hi"), 1)
    fmt.Printf("Replace first 'Hello' with 'Hi': %s\n", string(replaceFirst))
}
```

### Example 6: Working with Individual Bytes

```go
package main

import (
    "fmt"
)

func main() {
    data := []byte("Hello, World! 123")
    
    // Iterating through bytes
    fmt.Println("Iterating through bytes:")
    for i, b := range data {
        fmt.Printf("Index %2d: byte %3d (0x%02X) = '%c'\n", i, b, b, b)
    }
    
    // Categorizing bytes
    var letters, digits, punctuation, spaces []byte
    
    for _, b := range data {
        switch {
        case b >= 'A' && b <= 'Z' || b >= 'a' && b <= 'z':
            letters = append(letters, b)
        case b >= '0' && b <= '9':
            digits = append(digits, b)
        case b == ' ' || b == '\t' || b == '\n':
            spaces = append(spaces, b)
        default:
            punctuation = append(punctuation, b)
        }
    }
    
    fmt.Printf("\nCategorized bytes:\n")
    fmt.Printf("Letters: %s\n", string(letters))
    fmt.Printf("Digits: %s\n", string(digits))
    fmt.Printf("Punctuation: %s\n", string(punctuation))
    fmt.Printf("Spaces: %d space(s)\n", len(spaces))
    
    // Byte manipulation
    fmt.Println("\nByte manipulation:")
    
    // Convert to uppercase
    var uppercase []byte
    for _, b := range []byte("hello") {
        if b >= 'a' && b <= 'z' {
            uppercase = append(uppercase, b-32) // Convert to uppercase
        } else {
            uppercase = append(uppercase, b)
        }
    }
    fmt.Printf("Uppercase: %s\n", string(uppercase))
    
    // XOR with a key
    message := []byte("secret")
    key := byte(42)
    var encrypted []byte
    for _, b := range message {
        encrypted = append(encrypted, b^key)
    }
    fmt.Printf("Encrypted: %v\n", encrypted)
    
    // Decrypt (XOR again with same key)
    var decrypted []byte
    for _, b := range encrypted {
        decrypted = append(decrypted, b^key)
    }
    fmt.Printf("Decrypted: %s\n", string(decrypted))
}
```

### Example 7: Byte Slice Growing and Shrinking

```go
package main

import (
    "fmt"
)

func main() {
    // Start with empty slice
    var data []byte
    fmt.Printf("Initial: len=%d, cap=%d\n", len(data), cap(data))
    
    // Append single bytes
    data = append(data, 'H', 'e', 'l', 'l', 'o')
    fmt.Printf("After adding 'Hello': len=%d, cap=%d, data=%s\n", 
        len(data), cap(data), string(data))
    
    // Append slice
    data = append(data, []byte(", World!")...)
    fmt.Printf("After adding ', World!': len=%d, cap=%d, data=%s\n", 
        len(data), cap(data), string(data))
    
    // Pre-allocate for performance
    optimized := make([]byte, 0, 100) // length 0, capacity 100
    optimized = append(optimized, []byte("Pre-allocated slice")...)
    fmt.Printf("Optimized: len=%d, cap=%d, data=%s\n", 
        len(optimized), cap(optimized), string(optimized))
    
    // Shrinking slice (removing elements)
    fmt.Println("\nShrinking operations:")
    original := []byte("Hello, World!")
    fmt.Printf("Original: %s\n", string(original))
    
    // Remove first 7 characters
    shortened := original[7:]
    fmt.Printf("Remove first 7: %s\n", string(shortened))
    
    // Remove last 6 characters
    shortened2 := original[:len(original)-6]
    fmt.Printf("Remove last 6: %s\n", string(shortened2))
    
    // Remove middle part (remove ", " from "Hello, World!")
    middle_removed := append(original[:5], original[7:]...)
    fmt.Printf("Remove middle: %s\n", string(middle_removed))
    
    // Efficient way to remove element at index
    removeAtIndex := func(slice []byte, index int) []byte {
        if index < 0 || index >= len(slice) {
            return slice
        }
        return append(slice[:index], slice[index+1:]...)
    }
    
    test := []byte("ABCDEFGH")
    test = removeAtIndex(test, 3) // Remove 'D'
    fmt.Printf("After removing index 3: %s\n", string(test))
}
```

### Example 8: Memory-Efficient Byte Operations

```go
package main

import (
    "fmt"
    "runtime"
)

// getMemUsage returns the current memory usage
func getMemUsage() (float64, float64) {
    var m runtime.MemStats
    runtime.GC()
    runtime.ReadMemStats(&m)
    return float64(m.Alloc) / 1024 / 1024, float64(m.Sys) / 1024 / 1024
}

func main() {
    fmt.Println("Memory-Efficient Byte Operations")
    
    // Inefficient way - creates many intermediate slices
    fmt.Println("\n1. Inefficient concatenation:")
    alloc1, sys1 := getMemUsage()
    
    var result []byte
    for i := 0; i < 1000; i++ {
        result = append(result, []byte(fmt.Sprintf("Item%d ", i))...)
    }
    
    alloc2, sys2 := getMemUsage()
    fmt.Printf("Inefficient - Alloc: %.2f MB (diff: %.2f), Sys: %.2f MB\n", 
        alloc2, alloc2-alloc1, sys2)
    
    // Efficient way - pre-allocate capacity
    fmt.Println("\n2. Efficient concatenation:")
    alloc3, _ := getMemUsage()
    
    efficient := make([]byte, 0, 10000) // Pre-allocate capacity
    for i := 0; i < 1000; i++ {
        efficient = append(efficient, []byte(fmt.Sprintf("Item%d ", i))...)
    }
    
    alloc4, sys4 := getMemUsage()
    fmt.Printf("Efficient - Alloc: %.2f MB (diff: %.2f), Sys: %.2f MB\n", 
        alloc4, alloc4-alloc3, sys4)
    
    // Using sync.Pool for byte slice reuse
    fmt.Println("\n3. Reusing byte slices:")
    
    type ByteSlicePool struct {
        pool [][]byte
    }
    
    func (p *ByteSlicePool) Get(size int) []byte {
        if len(p.pool) > 0 {
            // Reuse existing slice
            slice := p.pool[len(p.pool)-1]
            p.pool = p.pool[:len(p.pool)-1]
            
            if cap(slice) >= size {
                return slice[:0] // Reset length but keep capacity
            }
        }
        // Create new slice if pool is empty or existing slice too small
        return make([]byte, 0, size)
    }
    
    func (p *ByteSlicePool) Put(slice []byte) {
        if cap(slice) > 0 {
            p.pool = append(p.pool, slice)
        }
    }
    
    pool := &ByteSlicePool{}
    
    // Simulate multiple operations with slice reuse
    for round := 0; round < 5; round++ {
        slice := pool.Get(100)
        slice = append(slice, []byte(fmt.Sprintf("Round %d data", round))...)
        fmt.Printf("Round %d: len=%d, cap=%d, data=%s\n", 
            round, len(slice), cap(slice), string(slice))
        pool.Put(slice)
    }
}
```

### Example 9: Byte Slice Sorting and Ordering

```go
package main

import (
    "bytes"
    "fmt"
    "sort"
)

func main() {
    // Sorting byte slices
    data := [][]byte{
        []byte("zebra"),
        []byte("apple"),
        []byte("banana"),
        []byte("cherry"),
    }
    
    fmt.Println("Original order:")
    for i, item := range data {
        fmt.Printf("%d: %s\n", i, string(item))
    }
    
    // Sort using bytes.Compare
    sort.Slice(data, func(i, j int) bool {
        return bytes.Compare(data[i], data[j]) < 0
    })
    
    fmt.Println("\nSorted order:")
    for i, item := range data {
        fmt.Printf("%d: %s\n", i, string(item))
    }
    
    // Custom sorting - by length first, then alphabetically
    data2 := [][]byte{
        []byte("cat"),
        []byte("elephant"),
        []byte("dog"),
        []byte("ant"),
        []byte("butterfly"),
    }
    
    sort.Slice(data2, func(i, j int) bool {
        if len(data2[i]) != len(data2[j]) {
            return len(data2[i]) < len(data2[j])
        }
        return bytes.Compare(data2[i], data2[j]) < 0
    })
    
    fmt.Println("\nSorted by length then alphabetically:")
    for i, item := range data2 {
        fmt.Printf("%d: %s (len=%d)\n", i, string(item), len(item))
    }
    
    // Sorting individual bytes within a slice
    singleSlice := []byte("hello")
    fmt.Printf("\nBefore sorting bytes: %s\n", string(singleSlice))
    
    sort.Slice(singleSlice, func(i, j int) bool {
        return singleSlice[i] < singleSlice[j]
    })
    
    fmt.Printf("After sorting bytes: %s\n", string(singleSlice))
    
    // Reverse sorting
    reverseData := [][]byte{
        []byte("first"),
        []byte("second"),
        []byte("third"),
    }
    
    sort.Slice(reverseData, func(i, j int) bool {
        return bytes.Compare(reverseData[i], reverseData[j]) > 0 // Note: > for reverse
    })
    
    fmt.Println("\nReverse sorted:")
    for i, item := range reverseData {
        fmt.Printf("%d: %s\n", i, string(item))
    }
}
```

### Example 10: Advanced Byte Slice Patterns

```go
package main

import (
    "fmt"
)

func main() {
    // Pattern 1: Circular buffer implementation
    fmt.Println("1. Circular Buffer:")
    
    type CircularBuffer struct {
        data  []byte
        start int
        end   int
        size  int
        cap   int
    }
    
    func NewCircularBuffer(capacity int) *CircularBuffer {
        return &CircularBuffer{
            data: make([]byte, capacity),
            cap:  capacity,
        }
    }
    
    func (cb *CircularBuffer) Write(b byte) bool {
        if cb.size == cb.cap {
            return false // Buffer full
        }
        cb.data[cb.end] = b
        cb.end = (cb.end + 1) % cb.cap
        cb.size++
        return true
    }
    
    func (cb *CircularBuffer) Read() (byte, bool) {
        if cb.size == 0 {
            return 0, false // Buffer empty
        }
        b := cb.data[cb.start]
        cb.start = (cb.start + 1) % cb.cap
        cb.size--
        return b, true
    }
    
    cb := NewCircularBuffer(5)
    for _, b := range []byte("Hello") {
        cb.Write(b)
    }
    
    for i := 0; i < 3; i++ {
        if b, ok := cb.Read(); ok {
            fmt.Printf("Read: %c\n", b)
        }
    }
    
    // Write more data
    cb.Write('X')
    cb.Write('Y')
    
    fmt.Print("Remaining: ")
    for {
        if b, ok := cb.Read(); ok {
            fmt.Printf("%c", b)
        } else {
            break
        }
    }
    fmt.Println()
    
    // Pattern 2: Byte slice interning (string-like optimization)
    fmt.Println("\n2. Byte Slice Interning:")
    
    type ByteIntern struct {
        cache map[string][]byte
    }
    
    func NewByteIntern() *ByteIntern {
        return &ByteIntern{cache: make(map[string][]byte)}
    }
    
    func (bi *ByteIntern) Intern(data []byte) []byte {
        key := string(data)
        if cached, exists := bi.cache[key]; exists {
            return cached
        }
        
        // Create a copy to avoid external modifications
        interned := make([]byte, len(data))
        copy(interned, data)
        bi.cache[key] = interned
        return interned
    }
    
    intern := NewByteIntern()
    
    // These will reuse the same underlying array
    s1 := intern.Intern([]byte("hello"))
    s2 := intern.Intern([]byte("hello"))
    s3 := intern.Intern([]byte("world"))
    
    fmt.Printf("s1 and s2 same underlying array: %t\n", &s1[0] == &s2[0])
    fmt.Printf("s1 and s3 different underlying array: %t\n", &s1[0] != &s3[0])
    
    // Pattern 3: Byte slice builder with efficient concatenation
    fmt.Println("\n3. Efficient Byte Builder:")
    
    type ByteBuilder struct {
        data []byte
    }
    
    func NewByteBuilder(initialCap int) *ByteBuilder {
        return &ByteBuilder{data: make([]byte, 0, initialCap)}
    }
    
    func (bb *ByteBuilder) Write(p []byte) {
        bb.data = append(bb.data, p...)
    }
    
    func (bb *ByteBuilder) WriteByte(b byte) {
        bb.data = append(bb.data, b)
    }
    
    func (bb *ByteBuilder) WriteString(s string) {
        bb.data = append(bb.data, []byte(s)...)
    }
    
    func (bb *ByteBuilder) Bytes() []byte {
        return bb.data
    }
    
    func (bb *ByteBuilder) String() string {
        return string(bb.data)
    }
    
    func (bb *ByteBuilder) Reset() {
        bb.data = bb.data[:0]
    }
    
    builder := NewByteBuilder(50)
    builder.WriteString("Hello")
    builder.WriteByte(' ')
    builder.Write([]byte("World"))
    builder.WriteByte('!')
    
    fmt.Printf("Built string: %s\n", builder.String())
    fmt.Printf("Length: %d, Capacity: %d\n", len(builder.Bytes()), cap(builder.Bytes()))
}
```

---

## Reading and Writing Binary Files

### Example 11: Basic Binary File Reading

```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    // Create a sample binary file
    createSampleFile()
    
    // Method 1: Read entire file at once
    fmt.Println("1. Reading entire file:")
    data, err := os.ReadFile("sample.bin")
    if err != nil {
        fmt.Printf("Error reading file: %v\n", err)
        return
    }
    
    fmt.Printf("File size: %d bytes\n", len(data))
    fmt.Printf("First 20 bytes: %v\n", data[:20])
    fmt.Printf("As hex: %x\n", data[:20])
    
    // Method 2: Reading with os.Open and manual buffer
    fmt.Println("\n2. Reading with buffer:")
    file, err := os.Open("sample.bin")
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        return
    }
    defer file.Close()
    
    buffer := make([]byte, 10)
    bytesRead, err := file.Read(buffer)
    if err != nil && err != io.EOF {
        fmt.Printf("Error reading: %v\n", err)
        return
    }
    
    fmt.Printf("Bytes read: %d\n", bytesRead)
    fmt.Printf("Buffer content: %v\n", buffer[:bytesRead])
    
    // Method 3: Reading chunk by chunk
    fmt.Println("\n3. Reading in chunks:")
    file.Seek(0, 0) // Reset to beginning
    
    chunkSize := 8
    chunk := make([]byte, chunkSize)
    chunkNum := 0
    
    for {
        n, err := file.Read(chunk)
        if err == io.EOF {
            break
        }
        if err != nil {
            fmt.Printf("Error reading chunk: %v\n", err)
            break
        }
        
        fmt.Printf("Chunk %d (%d bytes): %v\n", chunkNum, n, chunk[:n])
        chunkNum++
        
        if chunkNum >= 3 { // Limit output for demo
            break
        }
    }
    
    // Clean up
    os.Remove("sample.bin")
}

func createSampleFile() {
    data := make([]byte, 100)
    for i := range data {
        data[i] = byte(i % 256)
    }
    
    err := os.WriteFile("sample.bin", data, 0644)
    if err != nil {
        fmt.Printf("Error creating sample file: %v\n", err)
    }
}
```

### Example 12: Binary File Writing with Different Methods

```go
package main

import (
    "bufio"
    "fmt"
    "os"
)

func main() {
    // Method 1: Write entire slice at once
    fmt.Println("1. Writing entire slice:")
    data1 := []byte{0x00, 0x01, 0x02, 0x03, 0x04, 0x05}
    err := os.WriteFile("output1.bin", data1, 0644)
    if err != nil {
        fmt.Printf("Error writing file: %v\n", err)
        return
    }
    fmt.Printf("Wrote %d bytes to output1.bin\n", len(data1))
    
    // Method 2: Using os.Create and Write
    fmt.Println("\n2. Using os.Create:")
    file2, err := os.Create("output2.bin")
    if err != nil {
        fmt.Printf("Error creating file: %v\n", err)
        return
    }
    defer file2.Close()
    
    data2 := []byte("Binary data with text mixed in\x00\x01\x02")
    bytesWritten, err := file2.Write(data2)
    if err != nil {
        fmt.Printf("Error writing: %v\n", err)
        return
    }
    fmt.Printf("Wrote %d bytes to output2.bin\n", bytesWritten)
    
    // Method 3: Using buffered writer for better performance
    fmt.Println("\n3. Using buffered writer:")
    file3, err := os.Create("output3.bin")
    if err != nil {
        fmt.Printf("Error creating file: %v\n", err)
        return
    }
    defer file3.Close()
    
    writer := bufio.NewWriter(file3)
    defer writer.Flush()
    
    // Write in small chunks
    for i := 0; i < 1000; i++ {
        chunk := []byte{byte(i % 256), byte((i + 1) % 256)}
        _, err := writer.Write(chunk)
        if err != nil {
            fmt.Printf("Error writing chunk: %v\n", err)
            return
        }
    }
    fmt.Printf("Wrote 2000 bytes to output3.bin using buffered writer\n")
    
    // Method 4: Appending to existing file
    fmt.Println("\n4. Appending to file:")
    file4, err := os.OpenFile("output1.bin", os.O_APPEND|os.O_WRONLY, 0644)
    if err != nil {
        fmt.Printf("Error opening for append: %v\n", err)
        return
    }
    defer file4.Close()
    
    appendData := []byte{0xFF, 0xFE, 0xFD}
    _, err = file4.Write(appendData)
    if err != nil {
        fmt.Printf("Error appending: %v\n", err)
        return
    }
    fmt.Printf("Appended %d bytes to output1.bin\n", len(appendData))
    
    // Verify the files
    verifyFiles()
    
    // Clean up
    os.Remove("output1.bin")
    os.Remove("output2.bin")
    os.Remove("output3.bin")
}

func verifyFiles() {
    fmt.Println("\nVerifying files:")
    
    files := []string{"output1.bin", "output2.bin", "output3.bin"}
    
    for _, filename := range files {
        if info, err := os.Stat(filename); err == nil {
            fmt.Printf("%s: %d bytes\n", filename, info.Size())
            
            // Read first few bytes
            if data, err := os.ReadFile(filename); err == nil {
                if len(data) > 10 {
                    fmt.Printf("  First 10 bytes: %v\n", data[:10])
                } else {
                    fmt.Printf("  All bytes: %v\n", data)
                }
            }
        }
    }
}
```

### Example 13: Random Access Binary File Operations

```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    // Create a test file with structured data
    createTestFile()
    
    // Open file for random access
    file, err := os.OpenFile("test.bin", os.O_RDWR, 0644)
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        return
    }
    defer file.Close()
    
    // Get file size
    fileInfo, err := file.Stat()
    if err != nil {
        fmt.Printf("Error getting file info: %v\n", err)
        return
    }
    fmt.Printf("File size: %d bytes\n", fileInfo.Size())
    
    // Random read operations
    fmt.Println("\n1. Random read operations:")
    
    // Read from position 10
    buffer := make([]byte, 5)
    offset, err := file.Seek(10, io.SeekStart)
    if err != nil {
        fmt.Printf("Error seeking: %v\n", err)
        return
    }
    fmt.Printf("Seeked to position: %d\n", offset)
    
    n, err := file.Read(buffer)
    if err != nil {
        fmt.Printf("Error reading: %v\n", err)
        return
    }
    fmt.Printf("Read %d bytes: %v\n", n, buffer[:n])
    
    // Read from end of file
    offset, err = file.Seek(-5, io.SeekEnd)
    if err != nil {
        fmt.Printf("Error seeking from end: %v\n", err)
        return
    }
    fmt.Printf("Seeked to position (from end): %d\n", offset)
    
    n, err = file.Read(buffer)
    if err != nil && err != io.EOF {
        fmt.Printf("Error reading: %v\n", err)
        return
    }
    fmt.Printf("Read %d bytes from end: %v\n", n, buffer[:n])
    
    // Random write operations
    fmt.Println("\n2. Random write operations:")
    
    // Write at position 5
    _, err = file.Seek(5, io.SeekStart)
    if err != nil {
        fmt.Printf("Error seeking for write: %v\n", err)
        return
    }
    
    newData := []byte{0xAA, 0xBB, 0xCC}
    n, err = file.Write(newData)
    if err != nil {
        fmt.Printf("Error writing: %v\n", err)
        return
    }
    fmt.Printf("Wrote %d bytes at position 5\n", n)
    
    // Read back to verify
    _, err = file.Seek(0, io.SeekStart)
    if err != nil {
        fmt.Printf("Error seeking to start: %v\n", err)
        return
    }
    
    fullData := make([]byte, 20)
    n, err = file.Read(fullData)
    if err != nil && err != io.EOF {
        fmt.Printf("Error reading full data: %v\n", err)
        return
    }
    fmt.Printf("Full file content: %v\n", fullData[:n])
    
    // Get current position
    currentPos, err := file.Seek(0, io.SeekCurrent)
    if err != nil {
        fmt.Printf("Error getting current position: %v\n", err)
        return
    }
    fmt.Printf("Current position: %d\n", currentPos)
    
    // Clean up
    file.Close()
    os.Remove("test.bin")
}

func createTestFile() {
    data := make([]byte, 50)
    for i := range data {
        data[i] = byte(i)
    }
    
    err := os.WriteFile("test.bin", data, 0644)
    if err != nil {
        fmt.Printf("Error creating test file: %v\n", err)
    }
}
```

### Example 14: Binary File Streaming and Pipes

```go
package main

import (
    "fmt"
    "io"
    "os"
)

func main() {
    // Create test data
    testData := make([]byte, 10000)
    for i := range testData {
        testData[i] = byte(i % 256)
    }
    os.WriteFile("stream_test.bin", testData, 0644)
    
    // Streaming read with io.Copy
    fmt.Println("1. Streaming with io.Copy:")
    
    sourceFile, err := os.Open("stream_test.bin")
    if err != nil {
        fmt.Printf("Error opening source: %v\n", err)
        return
    }
    defer sourceFile.Close()
    
    destFile, err := os.Create("stream_copy.bin")
    if err != nil {
        fmt.Printf("Error creating destination: %v\n", err)
        return
    }
    defer destFile.Close()
    
    // Copy entire file
    bytesCopied, err := io.Copy(destFile, sourceFile)
    if err != nil {
        fmt.Printf("Error copying: %v\n", err)
        return
    }
    fmt.Printf("Copied %d bytes\n", bytesCopied)
    
    // Streaming read with limited buffer
    fmt.Println("\n2. Streaming with LimitReader:")
    
    sourceFile.Seek(0, 0) // Reset to beginning
    limitedReader := io.LimitReader(sourceFile, 100) // Only read first 100 bytes
    
    limitedFile, err := os.Create("limited.bin")
    if err != nil {
        fmt.Printf("Error creating limited file: %v\n", err)
        return
    }
    defer limitedFile.Close()
    
    bytesLimited, err := io.Copy(limitedFile, limitedReader)
    if err != nil {
        fmt.Printf("Error copying limited: %v\n", err)
        return
    }
    fmt.Printf("Limited copy: %d bytes\n", bytesLimited)
    
    // Using io.TeeReader to read and write simultaneously
    fmt.Println("\n3. Using TeeReader:")
    
    sourceFile.Seek(0, 0)
    teeFile, err := os.Create("tee_output.bin")
    if err != nil {
        fmt.Printf("Error creating tee file: %v\n", err)
        return
    }
    defer teeFile.Close()
    
    // TeeReader reads from source and writes to tee file
    teeReader := io.TeeReader(sourceFile, teeFile)
    
    // Read through TeeReader (this will also write to tee file)
    buffer := make([]byte, 50)
    n, err := teeReader.Read(buffer)
    if err != nil && err != io.EOF {
        fmt.Printf("Error reading with tee: %v\n", err)
        return
    }
    fmt.Printf("Read %d bytes through TeeReader\n", n)
    fmt.Printf("First 10 bytes: %v\n", buffer[:10])
    
    // Clean up
    os.Remove("stream_test.bin")
    os.Remove("stream_copy.bin")
    os.Remove("limited.bin")
    os.Remove("tee_output.bin")
}
```

### Example 15: Reading Structured Binary Data

```go
package main

import (
    "encoding/binary"
    "fmt"
    "os"
)

// FileHeader represents a simple binary file header
type FileHeader struct {
    Magic    uint32  // 4 bytes - file magic number
    Version  uint16  // 2 bytes - version
    Flags    uint16  // 2 bytes - flags
    FileSize uint64  // 8 bytes - total file size
    Reserved [16]byte // 16 bytes - reserved space
}

func main() {
    // Create a binary file with structured data
    createStructuredFile()
    
    // Read the structured data
    fmt.Println("Reading structured binary data:")
    
    file, err := os.Open("structured.bin")
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        return
    }
    defer file.Close()
    
    // Read header
    var header FileHeader
    err = binary.Read(file, binary.LittleEndian, &header)
    if err != nil {
        fmt.Printf("Error reading header: %v\n", err)
        return
    }
    
    fmt.Printf("Header:\n")
    fmt.Printf("  Magic: 0x%08X\n", header.Magic)
    fmt.Printf("  Version: %d\n", header.Version)
    fmt.Printf("  Flags: 0x%04X\n", header.Flags)
    fmt.Printf("  File Size: %d bytes\n", header.FileSize)
    fmt.Printf("  Reserved: %v\n", header.Reserved[:4]) // Show first 4 bytes
    
    // Read payload data
    payload := make([]byte, header.FileSize-uint64(binary.Size(header)))
    n, err := file.Read(payload)
    if err != nil {
        fmt.Printf("Error reading payload: %v\n", err)
        return
    }
    
    fmt.Printf("\nPayload (%d bytes): %s\n", n, string(payload))
    
    // Manual field reading (alternative approach)
    fmt.Println("\nManual field reading:")
    file.Seek(0, 0) // Reset to beginning
    
    var magic uint32
    binary.Read(file, binary.LittleEndian, &magic)
    fmt.Printf("Magic (manual): 0x%08X\n", magic)
    
    var version uint16
    binary.Read(file, binary.LittleEndian, &version)
    fmt.Printf("Version (manual): %d\n", version)
    
    // Clean up
    os.Remove("structured.bin")
}

func createStructuredFile() {
    file, err := os.Create("structured.bin")
    if err != nil {
        fmt.Printf("Error creating file: %v\n", err)
        return
    }
    defer file.Close()
    
    // Create header
    header := FileHeader{
        Magic:   0xDEADBEEF,
        Version: 1,
        Flags:   0x0001,
    }
    
    // Payload data
    payload := []byte("Hello, this is the payload data!")
    header.FileSize = uint64(binary.Size(header)) + uint64(len(payload))
    
    // Write header
    err = binary.Write(file, binary.LittleEndian, &header)
    if err != nil {
        fmt.Printf("Error writing header: %v\n", err)
        return
    }
    
    // Write payload
    _, err = file.Write(payload)
    if err != nil {
        fmt.Printf("Error writing payload: %v\n", err)
        return
    }
}
```

### Example 16: File Copying with Progress and Checksums

```go
package main

import (
    "crypto/md5"
    "fmt"
    "io"
    "os"
    "time"
)

func main() {
    // Create a large test file
    createLargeFile()
    
    // Copy with progress tracking
    fmt.Println("Copying file with progress tracking:")
    
    err := copyFileWithProgress("large_file.bin", "large_file_copy.bin")
    if err != nil {
        fmt.Printf("Error copying file: %v\n", err)
        return
    }
    
    // Verify files are identical using checksums
    fmt.Println("\nVerifying file integrity:")
    
    hash1, err := calculateMD5("large_file.bin")
    if err != nil {
        fmt.Printf("Error calculating hash for original: %v\n", err)
        return
    }
    
    hash2, err := calculateMD5("large_file_copy.bin")
    if err != nil {
        fmt.Printf("Error calculating hash for copy: %v\n", err)
        return
    }
    
    fmt.Printf("Original file MD5: %x\n", hash1)
    fmt.Printf("Copy file MD5:     %x\n", hash2)
    fmt.Printf("Files identical:   %t\n", string(hash1) == string(hash2))
    
    // Clean up
    os.Remove("large_file.bin")
    os.Remove("large_file_copy.bin")
}

func createLargeFile() {
    file, err := os.Create("large_file.bin")
    if err != nil {
        fmt.Printf("Error creating large file: %v\n", err)
        return
    }
    defer file.Close()
    
    // Write 1MB of data
    buffer := make([]byte, 1024) // 1KB buffer
    for i := range buffer {
        buffer[i] = byte(i % 256)
    }
    
    for i := 0; i < 1024; i++ { // Write 1024 times = 1MB
        file.Write(buffer)
    }
}

func copyFileWithProgress(src, dst string) error {
    sourceFile, err := os.Open(src)
    if err != nil {
        return err
    }
    defer sourceFile.Close()
    
    // Get source file size
    sourceInfo, err := sourceFile.Stat()
    if err != nil {
        return err
    }
    totalSize := sourceInfo.Size()
    
    destFile, err := os.Create(dst)
    if err != nil {
        return err
    }
    defer destFile.Close()
    
    // Create a progress reader
    progressReader := &ProgressReader{
        Reader:    sourceFile,
        Total:     totalSize,
        StartTime: time.Now(),
    }
    
    // Copy with progress
    _, err = io.Copy(destFile, progressReader)
    fmt.Println() // New line after progress
    
    return err
}

type ProgressReader struct {
    Reader    io.Reader
    Total     int64
    Current   int64
    StartTime time.Time
}

func (pr *ProgressReader) Read(p []byte) (int, error) {
    n, err := pr.Reader.Read(p)
    pr.Current += int64(n)
    
    // Print progress every 100KB
    if pr.Current%102400 == 0 || err == io.EOF {
        percent := float64(pr.Current) / float64(pr.Total) * 100
        elapsed := time.Since(pr.StartTime)
        speed := float64(pr.Current) / elapsed.Seconds() / 1024 // KB/s
        
        fmt.Printf("\rProgress: %.1f%% (%d/%d bytes) - %.1f KB/s", 
            percent, pr.Current, pr.Total, speed)
    }
    
    return n, err
}

func calculateMD5(filename string) ([]byte, error) {
    file, err := os.Open(filename)
    if err != nil {
        return nil, err
    }
    defer file.Close()
    
    hash := md5.New()
    _, err = io.Copy(hash, file)
    if err != nil {
        return nil, err
    }
    
    return hash.Sum(nil), nil
}
```

### Example 17: Memory-Mapped File Operations

```go
package main

import (
    "fmt"
    "os"
    "syscall"
    "unsafe"
)

func main() {
    // Create a test file
    createTestFile()
    
    // Memory map the file (Unix/Linux specific)
    fmt.Println("Memory-mapped file operations:")
    
    file, err := os.OpenFile("mmap_test.bin", os.O_RDWR, 0644)
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        return
    }
    defer file.Close()
    
    // Get file info
    fileInfo, err := file.Stat()
    if err != nil {
        fmt.Printf("Error getting file info: %v\n", err)
        return
    }
    fileSize := int(fileInfo.Size())
    
    // Memory map the file
    data, err := syscall.Mmap(int(file.Fd()), 0, fileSize, syscall.PROT_READ|syscall.PROT_WRITE, syscall.MAP_SHARED)
    if err != nil {
        fmt.Printf("Error memory mapping: %v\n", err)
        return
    }
    defer syscall.Munmap(data)
    
    fmt.Printf("Memory-mapped %d bytes\n", len(data))
    fmt.Printf("First 10 bytes: %v\n", data[:10])
    
    // Modify data directly in memory
    for i := 0; i < 10; i++ {
        data[i] = byte(255 - i)
    }
    
    // Sync changes to disk
    err = syscall.Msync(data, syscall.MS_SYNC)
    if err != nil {
        fmt.Printf("Error syncing: %v\n", err)
        return
    }
    
    fmt.Printf("Modified first 10 bytes: %v\n", data[:10])
    
    // Alternative approach using unsafe (for demonstration - be careful!)
    fmt.Println("\nUsing unsafe pointer operations:")
    
    // Treat memory-mapped data as a slice of uint32
    uint32Slice := (*[256]uint32)(unsafe.Pointer(&data[0]))[:len(data)/4]
    fmt.Printf("First uint32: %d (0x%08X)\n", uint32Slice[0], uint32Slice[0])
    
    // Modify as uint32
    uint32Slice[0] = 0xDEADBEEF
    fmt.Printf("After modification: %d (0x%08X)\n", uint32Slice[0], uint32Slice[0])
    fmt.Printf("Corresponding bytes: %v\n", data[:4])
    
    // Clean up
    os.Remove("mmap_test.bin")
}

func createTestFile() {
    data := make([]byte, 1024)
    for i := range data {
        data[i] = byte(i % 256)
    }
    
    err := os.WriteFile("mmap_test.bin", data, 0644)
    if err != nil {
        fmt.Printf("Error creating test file: %v\n", err)
    }
}
```

### Example 18: Concurrent File Processing

```go
package main

import (
    "fmt"
    "io"
    "os"
    "sync"
    "time"
)

func main() {
    // Create multiple test files
    createMultipleFiles()
    
    // Process files concurrently
    fmt.Println("Processing files concurrently:")
    
    files := []string{"file1.bin", "file2.bin", "file3.bin", "file4.bin"}
    
    // Sequential processing
    start := time.Now()
    sequentialResults := processFilesSequential(files)
    sequentialTime := time.Since(start)
    
    fmt.Printf("Sequential processing took: %v\n", sequentialTime)
    for i, result := range sequentialResults {
        fmt.Printf("  File %d: %d bytes\n", i+1, result)
    }
    
    // Concurrent processing
    start = time.Now()
    concurrentResults := processFilesConcurrent(files)
    concurrentTime := time.Since(start)
    
    fmt.Printf("\nConcurrent processing took: %v\n", concurrentTime)
    for i, result := range concurrentResults {
        fmt.Printf("  File %d: %d bytes\n", i+1, result)
    }
    
    fmt.Printf("\nSpeedup: %.2fx\n", float64(sequentialTime)/float64(concurrentTime))
    
    // Clean up
    for _, filename := range files {
        os.Remove(filename)
    }
}

func createMultipleFiles() {
    for i := 1; i <= 4; i++ {
        filename := fmt.Sprintf("file%d.bin", i)
        data := make([]byte, 10000*i) // Different sizes
        
        for j := range data {
            data[j] = byte(j % 256)
        }
        
        os.WriteFile(filename, data, 0644)
    }
}

func processFilesSequential(files []string) []int {
    results := make([]int, len(files))
    
    for i, filename := range files {
        results[i] = processFile(filename)
    }
    
    return results
}

func processFilesConcurrent(files []string) []int {
    results := make([]int, len(files))
    var wg sync.WaitGroup
    
    for i, filename := range files {
        wg.Add(1)
        go func(index int, fname string) {
            defer wg.Done()
            results[index] = processFile(fname)
        }(i, filename)
    }
    
    wg.Wait()
    return results
}

func processFile(filename string) int {
    // Simulate some processing by reading file and counting bytes
    file, err := os.Open(filename)
    if err != nil {
        return 0
    }
    defer file.Close()
    
    var totalBytes int
    buffer := make([]byte, 1024)
    
    for {
        n, err := file.Read(buffer)
        totalBytes += n
        
        // Simulate processing time
        time.Sleep(time.Millisecond * 10)
        
        if err == io.EOF {
            break
        }
        if err != nil {
            return 0
        }
    }
    
    return totalBytes
}
```

### Example 19: Binary File Compression and Decompression

```go
package main

import (
    "compress/gzip"
    "fmt"
    "io"
    "os"
)

func main() {
    // Create test data
    testData := make([]byte, 10000)
    for i := range testData {
        // Create some patterns for better compression
        if i%100 < 50 {
            testData[i] = 0xAA
        } else {
            testData[i] = byte(i % 256)
        }
    }
    
    err := os.WriteFile("original.bin", testData, 0644)
    if err != nil {
        fmt.Printf("Error writing original file: %v\n", err)
        return
    }
    
    // Compress the file
    fmt.Println("Compressing file:")
    err = compressFile("original.bin", "compressed.gz")
    if err != nil {
        fmt.Printf("Error compressing: %v\n", err)
        return
    }
    
    // Check file sizes
    originalInfo, _ := os.Stat("original.bin")
    compressedInfo, _ := os.Stat("compressed.gz")
    
    fmt.Printf("Original size: %d bytes\n", originalInfo.Size())
    fmt.Printf("Compressed size: %d bytes\n", compressedInfo.Size())
    fmt.Printf("Compression ratio: %.2f%%\n", 
        float64(compressedInfo.Size())/float64(originalInfo.Size())*100)
    
    // Decompress the file
    fmt.Println("\nDecompressing file:")
    err = decompressFile("compressed.gz", "decompressed.bin")
    if err != nil {
        fmt.Printf("Error decompressing: %v\n", err)
        return
    }
    
    // Verify decompressed file
    decompressedData, err := os.ReadFile("decompressed.bin")
    if err != nil {
        fmt.Printf("Error reading decompressed file: %v\n", err)
        return
    }
    
    // Compare with original
    identical := len(testData) == len(decompressedData)
    if identical {
        for i := range testData {
            if testData[i] != decompressedData[i] {
                identical = false
                break
            }
        }
    }
    
    fmt.Printf("Decompressed file size: %d bytes\n", len(decompressedData))
    fmt.Printf("Files identical: %t\n", identical)
    
    // Clean up
    os.Remove("original.bin")
    os.Remove("compressed.gz")
    os.Remove("decompressed.bin")
}

func compressFile(src, dst string) error {
    // Open source file
    sourceFile, err := os.Open(src)
    if err != nil {
        return err
    }
    defer sourceFile.Close()
    
    // Create destination file
    destFile, err := os.Create(dst)
    if err != nil {
        return err
    }
    defer destFile.Close()
    
    // Create gzip writer
    gzipWriter := gzip.NewWriter(destFile)
    defer gzipWriter.Close()
    
    // Copy and compress
    _, err = io.Copy(gzipWriter, sourceFile)
    return err
}

func decompressFile(src, dst string) error {
    // Open compressed file
    sourceFile, err := os.Open(src)
    if err != nil {
        return err
    }
    defer sourceFile.Close()
    
    // Create gzip reader
    gzipReader, err := gzip.NewReader(sourceFile)
    if err != nil {
        return err
    }
    defer gzipReader.Close()
    
    // Create destination file
    destFile, err := os.Create(dst)
    if err != nil {
        return err
    }
    defer destFile.Close()
    
    // Decompress and copy
    _, err = io.Copy(destFile, gzipReader)
    return err
}
```

### Example 20: File Format Detection and Validation

```go
package main

import (
    "bytes"
    "fmt"
    "os"
)

// FileSignature represents a file format signature
type FileSignature struct {
    Name      string
    Signature []byte
    Offset    int
}

func main() {
    // Define common file signatures
    signatures := []FileSignature{
        {"PNG", []byte{0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A}, 0},
        {"JPEG", []byte{0xFF, 0xD8, 0xFF}, 0},
        {"GIF87a", []byte{0x47, 0x49, 0x46, 0x38, 0x37, 0x61}, 0},
        {"GIF89a", []byte{0x47, 0x49, 0x46, 0x38, 0x39, 0x61}, 0},
        {"PDF", []byte{0x25, 0x50, 0x44, 0x46}, 0},
        {"ZIP", []byte{0x50, 0x4B, 0x03, 0x04}, 0},
        {"ELF", []byte{0x7F, 0x45, 0x4C, 0x46}, 0},
        {"PE", []byte{0x4D, 0x5A}, 0}, // DOS header
    }
    
    // Create test files with different signatures
    createTestFiles()
    
    // Test file detection
    testFiles := []string{
        "test_png.bin",
        "test_jpeg.bin", 
        "test_pdf.bin",
        "test_unknown.bin",
    }
    
    fmt.Println("File format detection:")
    
    for _, filename := range testFiles {
        fmt.Printf("\nAnalyzing %s:\n", filename)
        
        // Read file header
        file, err := os.Open(filename)
        if err != nil {
            fmt.Printf("  Error opening file: %v\n", err)
            continue
        }
        
        header := make([]byte, 256) // Read first 256 bytes
        n, err := file.Read(header)
        file.Close()
        
        if err != nil {
            fmt.Printf("  Error reading header: %v\n", err)
            continue
        }
        
        header = header[:n]
        fmt.Printf("  File size: %d bytes\n", n)
        fmt.Printf("  First 16 bytes: %v\n", header[:min(16, len(header))])
        fmt.Printf("  First 16 bytes (hex): %X\n", header[:min(16, len(header))])
        
        // Check against known signatures
        detected := false
        for _, sig := range signatures {
            if matchesSignature(header, sig) {
                fmt.Printf("  Detected format: %s\n", sig.Name)
                detected = true
                break
            }
        }
        
        if !detected {
            fmt.Printf("  Format: Unknown\n")
            
            // Try to guess based on content
            if isTextFile(header) {
                fmt.Printf("  Likely: Text file\n")
            } else {
                fmt.Printf("  Likely: Binary file\n")
            }
        }
    }
    
    // Clean up
    for _, filename := range testFiles {
        os.Remove(filename)
    }
}

func createTestFiles() {
    // Create PNG-like file
    pngData := []byte{0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A}
    pngData = append(pngData, bytes.Repeat([]byte{0x00}, 100)...)
    os.WriteFile("test_png.bin", pngData, 0644)
    
    // Create JPEG-like file
    jpegData := []byte{0xFF, 0xD8, 0xFF, 0xE0}
    jpegData = append(jpegData, bytes.Repeat([]byte{0x00}, 100)...)
    os.WriteFile("test_jpeg.bin", jpegData, 0644)
    
    // Create PDF-like file
    pdfData := []byte{0x25, 0x50, 0x44, 0x46, 0x2D, 0x31, 0x2E, 0x34}
    pdfData = append(pdfData, bytes.Repeat([]byte{0x00}, 100)...)
    os.WriteFile("test_pdf.bin", pdfData, 0644)
    
    // Create unknown format
    unknownData := []byte{0x12, 0x34, 0x56, 0x78}
    unknownData = append(unknownData, bytes.Repeat([]byte{0xAB}, 100)...)
    os.WriteFile("test_unknown.bin", unknownData, 0644)
}

func matchesSignature(data []byte, sig FileSignature) bool {
    if len(data) < sig.Offset+len(sig.Signature) {
        return false
    }
    
    return bytes.Equal(data[sig.Offset:sig.Offset+len(sig.Signature)], sig.Signature)
}

func isTextFile(data []byte) bool {
    // Simple heuristic: check if most bytes are printable ASCII
    printable := 0
    for _, b := range data {
        if (b >= 32 && b <= 126) || b == 9 || b == 10 || b == 13 {
            printable++
        }
    }
    
    return float64(printable)/float64(len(data)) > 0.8
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
```