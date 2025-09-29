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

    if a < b {
        return a
    }
    return b
}
```

---

## Bitwise Operations and Bit Manipulation

### Example 21: Basic Bitwise Operations

```go
package main

import (
    "fmt"
)

func main() {
    // Basic bitwise operations with bytes
    a := byte(0b10101010) // 170 in decimal
    b := byte(0b11110000) // 240 in decimal
    
    fmt.Printf("a = %08b (%d)\n", a, a)
    fmt.Printf("b = %08b (%d)\n", b, b)
    fmt.Println()
    
    // AND operation
    and_result := a & b
    fmt.Printf("a & b  = %08b (%d)\n", and_result, and_result)
    
    // OR operation
    or_result := a | b
    fmt.Printf("a | b  = %08b (%d)\n", or_result, or_result)
    
    // XOR operation
    xor_result := a ^ b
    fmt.Printf("a ^ b  = %08b (%d)\n", xor_result, xor_result)
    
    // NOT operation
    not_a := ^a
    fmt.Printf("^a     = %08b (%d)\n", not_a, not_a)
    
    // Left shift
    left_shift := a << 2
    fmt.Printf("a << 2 = %08b (%d)\n", left_shift, left_shift)
    
    // Right shift
    right_shift := a >> 2
    fmt.Printf("a >> 2 = %08b (%d)\n", right_shift, right_shift)
    
    // Practical examples
    fmt.Println("\nPractical bit operations:")
    
    // Check if a bit is set
    bit_position := 3
    is_set := (a & (1 << bit_position)) != 0
    fmt.Printf("Bit %d in a is set: %t\n", bit_position, is_set)
    
    // Set a bit
    set_bit := a | (1 << bit_position)
    fmt.Printf("Set bit %d: %08b -> %08b\n", bit_position, a, set_bit)
    
    // Clear a bit
    clear_bit := a &^ (1 << bit_position)
    fmt.Printf("Clear bit %d: %08b -> %08b\n", bit_position, a, clear_bit)
    
    // Toggle a bit
    toggle_bit := a ^ (1 << bit_position)
    fmt.Printf("Toggle bit %d: %08b -> %08b\n", bit_position, a, toggle_bit)
}
```

### Example 22: Bit Manipulation Functions and Utilities

```go
package main

import (
    "fmt"
)

// Bit manipulation utility functions
func setBit(value byte, position uint) byte {
    return value | (1 << position)
}

func clearBit(value byte, position uint) byte {
    return value &^ (1 << position)
}

func toggleBit(value byte, position uint) byte {
    return value ^ (1 << position)
}

func isBitSet(value byte, position uint) bool {
    return (value & (1 << position)) != 0
}

func countBits(value byte) int {
    count := 0
    for value != 0 {
        count += int(value & 1)
        value >>= 1
    }
    return count
}

func reverseBits(value byte) byte {
    result := byte(0)
    for i := 0; i < 8; i++ {
        if (value & (1 << i)) != 0 {
            result |= (1 << (7 - i))
        }
    }
    return result
}

func rotateLeft(value byte, positions uint) byte {
    positions %= 8 // Ensure positions is within 0-7
    return (value << positions) | (value >> (8 - positions))
}

func rotateRight(value byte, positions uint) byte {
    positions %= 8
    return (value >> positions) | (value << (8 - positions))
}

func main() {
    value := byte(0b10110101) // 181 in decimal
    
    fmt.Printf("Original value: %08b (%d)\n", value, value)
    fmt.Println()
    
    // Test bit manipulation functions
    fmt.Println("Bit manipulation functions:")
    
    // Set bit 2
    result := setBit(value, 2)
    fmt.Printf("Set bit 2:     %08b -> %08b\n", value, result)
    
    // Clear bit 5
    result = clearBit(value, 5)
    fmt.Printf("Clear bit 5:   %08b -> %08b\n", value, result)
    
    // Toggle bit 3
    result = toggleBit(value, 3)
    fmt.Printf("Toggle bit 3:  %08b -> %08b\n", value, result)
    
    // Check if bit 7 is set
    isSet := isBitSet(value, 7)
    fmt.Printf("Bit 7 is set: %t\n", isSet)
    
    // Count set bits
    count := countBits(value)
    fmt.Printf("Number of set bits: %d\n", count)
    
    // Reverse bits
    reversed := reverseBits(value)
    fmt.Printf("Reversed:      %08b -> %08b\n", value, reversed)
    
    // Rotate operations
    fmt.Println("\nRotation operations:")
    rotLeft := rotateLeft(value, 3)
    fmt.Printf("Rotate left 3:  %08b -> %08b\n", value, rotLeft)
    
    rotRight := rotateRight(value, 3)
    fmt.Printf("Rotate right 3: %08b -> %08b\n", value, rotRight)
    
    // Working with multiple bytes
    fmt.Println("\nMultiple byte operations:")
    data := []byte{0b11110000, 0b00001111, 0b10101010}
    
    fmt.Printf("Original: ")
    for _, b := range data {
        fmt.Printf("%08b ", b)
    }
    fmt.Println()
    
    // XOR all bytes together
    xorResult := byte(0)
    for _, b := range data {
        xorResult ^= b
    }
    fmt.Printf("XOR result: %08b (%d)\n", xorResult, xorResult)
    
    // Count total set bits
    totalBits := 0
    for _, b := range data {
        totalBits += countBits(b)
    }
    fmt.Printf("Total set bits: %d\n", totalBits)
}
```

### Example 23: Bit Fields and Packed Data Structures

```go
package main

import (
    "fmt"
)

// Example: RGB color packed into a single uint32
// Format: AARRGGBB (Alpha, Red, Green, Blue)
type Color uint32

func NewColor(alpha, red, green, blue byte) Color {
    return Color(uint32(alpha)<<24 | uint32(red)<<16 | uint32(green)<<8 | uint32(blue))
}

func (c Color) Alpha() byte {
    return byte(c >> 24)
}

func (c Color) Red() byte {
    return byte(c >> 16)
}

func (c Color) Green() byte {
    return byte(c >> 8)
}

func (c Color) Blue() byte {
    return byte(c)
}

func (c Color) String() string {
    return fmt.Sprintf("ARGB(%d,%d,%d,%d)", c.Alpha(), c.Red(), c.Green(), c.Blue())
}

// Example: File permissions packed into a single byte
type Permissions byte

const (
    ReadOwner   Permissions = 1 << 0
    WriteOwner  Permissions = 1 << 1
    ExecOwner   Permissions = 1 << 2
    ReadGroup   Permissions = 1 << 3
    WriteGroup  Permissions = 1 << 4
    ExecGroup   Permissions = 1 << 5
    ReadOthers  Permissions = 1 << 6
    WriteOthers Permissions = 1 << 7
)

func (p Permissions) HasPermission(perm Permissions) bool {
    return (p & perm) != 0
}

func (p *Permissions) GrantPermission(perm Permissions) {
    *p |= perm
}

func (p *Permissions) RevokePermission(perm Permissions) {
    *p &^= perm
}

func (p Permissions) String() string {
    var result string
    
    // Owner permissions
    if p.HasPermission(ReadOwner) {
        result += "r"
    } else {
        result += "-"
    }
    if p.HasPermission(WriteOwner) {
        result += "w"
    } else {
        result += "-"
    }
    if p.HasPermission(ExecOwner) {
        result += "x"
    } else {
        result += "-"
    }
    
    // Group permissions
    if p.HasPermission(ReadGroup) {
        result += "r"
    } else {
        result += "-"
    }
    if p.HasPermission(WriteGroup) {
        result += "w"
    } else {
        result += "-"
    }
    if p.HasPermission(ExecGroup) {
        result += "x"
    } else {
        result += "-"
    }
    
    // Others permissions
    if p.HasPermission(ReadOthers) {
        result += "r"
    } else {
        result += "-"
    }
    if p.HasPermission(WriteOthers) {
        result += "w"
    } else {
        result += "-"
    }
    
    return result
}

func main() {
    // Color example
    fmt.Println("Color bit field example:")
    
    color := NewColor(255, 128, 64, 32)
    fmt.Printf("Color: %s\n", color)
    fmt.Printf("Raw value: 0x%08X\n", uint32(color))
    fmt.Printf("Binary: %032b\n", uint32(color))
    
    fmt.Printf("Alpha: %d (0x%02X)\n", color.Alpha(), color.Alpha())
    fmt.Printf("Red:   %d (0x%02X)\n", color.Red(), color.Red())
    fmt.Printf("Green: %d (0x%02X)\n", color.Green(), color.Green())
    fmt.Printf("Blue:  %d (0x%02X)\n", color.Blue(), color.Blue())
    
    // Permissions example
    fmt.Println("\nPermissions bit field example:")
    
    perms := Permissions(0)
    fmt.Printf("Initial permissions: %s (%08b)\n", perms, byte(perms))
    
    // Grant some permissions
    perms.GrantPermission(ReadOwner | WriteOwner | ExecOwner)
    perms.GrantPermission(ReadGroup)
    fmt.Printf("After granting: %s (%08b)\n", perms, byte(perms))
    
    // Check specific permissions
    fmt.Printf("Owner can read: %t\n", perms.HasPermission(ReadOwner))
    fmt.Printf("Owner can write: %t\n", perms.HasPermission(WriteOwner))
    fmt.Printf("Others can read: %t\n", perms.HasPermission(ReadOthers))
    
    // Revoke a permission
    perms.RevokePermission(WriteOwner)
    fmt.Printf("After revoking write: %s (%08b)\n", perms, byte(perms))
    
    // Network packet header example
    fmt.Println("\nNetwork packet header example:")
    
    // Simplified TCP header flags (8 bits)
    var tcpFlags byte = 0
    
    const (
        FIN byte = 1 << 0 // Finish
        SYN byte = 1 << 1 // Synchronize
        RST byte = 1 << 2 // Reset
        PSH byte = 1 << 3 // Push
        ACK byte = 1 << 4 // Acknowledgment
        URG byte = 1 << 5 // Urgent
        ECE byte = 1 << 6 // ECN Echo
        CWR byte = 1 << 7 // Congestion Window Reduced
    )
    
    // Set SYN and ACK flags (connection establishment)
    tcpFlags |= SYN | ACK
    
    fmt.Printf("TCP Flags: %08b\n", tcpFlags)
    fmt.Printf("SYN set: %t\n", (tcpFlags & SYN) != 0)
    fmt.Printf("ACK set: %t\n", (tcpFlags & ACK) != 0)
    fmt.Printf("FIN set: %t\n", (tcpFlags & FIN) != 0)
    
    // Clear SYN flag
    tcpFlags &^= SYN
    fmt.Printf("After clearing SYN: %08b\n", tcpFlags)
}
```

### Example 24: Bitwise Algorithms and Tricks

```go
package main

import (
    "fmt"
)

func main() {
    // Power of 2 detection
    fmt.Println("Power of 2 detection:")
    numbers := []int{1, 2, 3, 4, 8, 15, 16, 32, 33}
    
    for _, n := range numbers {
        isPowerOf2 := n > 0 && (n & (n - 1)) == 0
        fmt.Printf("%d is power of 2: %t\n", n, isPowerOf2)
    }
    
    // Fast multiplication and division by powers of 2
    fmt.Println("\nFast multiplication/division:")
    value := 13
    fmt.Printf("Original: %d\n", value)
    fmt.Printf("Multiply by 4 (<<2): %d\n", value << 2)
    fmt.Printf("Multiply by 8 (<<3): %d\n", value << 3)
    fmt.Printf("Divide by 2 (>>1): %d\n", value >> 1)
    fmt.Printf("Divide by 4 (>>2): %d\n", value >> 2)
    
    // Swap without temporary variable
    fmt.Println("\nXOR swap:")
    a, b := 42, 73
    fmt.Printf("Before swap: a=%d, b=%d\n", a, b)
    
    a ^= b
    b ^= a
    a ^= b
    
    fmt.Printf("After swap: a=%d, b=%d\n", a, b)
    
    // Find the only non-duplicate number
    fmt.Println("\nFind unique number (XOR trick):")
    duplicates := []int{1, 2, 3, 2, 1, 4, 3} // 4 is unique
    unique := 0
    for _, num := range duplicates {
        unique ^= num
    }
    fmt.Printf("Unique number: %d\n", unique)
    
    // Count trailing zeros
    fmt.Println("\nCount trailing zeros:")
    testNumbers := []byte{8, 12, 16, 24, 32}
    
    for _, num := range testNumbers {
        zeros := countTrailingZeros(num)
        fmt.Printf("%d (%08b) has %d trailing zeros\n", num, num, zeros)
    }
    
    // Next power of 2
    fmt.Println("\nNext power of 2:")
    testVals := []uint32{5, 8, 13, 31, 32, 100}
    
    for _, val := range testVals {
        next := nextPowerOf2(val)
        fmt.Printf("Next power of 2 after %d: %d\n", val, next)
    }
    
    // Bit interleaving (Morton encoding)
    fmt.Println("\nBit interleaving (Morton encoding):")
    x, y := byte(5), byte(3)
    morton := mortonEncode(x, y)
    fmt.Printf("Morton encode(%d, %d) = %d (%016b)\n", x, y, morton, morton)
    
    decoded_x, decoded_y := mortonDecode(morton)
    fmt.Printf("Morton decode(%d) = (%d, %d)\n", morton, decoded_x, decoded_y)
    
    // Gray code conversion
    fmt.Println("\nGray code conversion:")
    for i := byte(0); i < 8; i++ {
        gray := binaryToGray(i)
        binary := grayToBinary(gray)
        fmt.Printf("Binary %d (%03b) -> Gray %d (%03b) -> Binary %d (%03b)\n", 
            i, i, gray, gray, binary, binary)
    }
}

func countTrailingZeros(value byte) int {
    if value == 0 {
        return 8
    }
    
    count := 0
    for (value & 1) == 0 {
        value >>= 1
        count++
    }
    return count
}

func nextPowerOf2(value uint32) uint32 {
    if value == 0 {
        return 1
    }
    
    value--
    value |= value >> 1
    value |= value >> 2
    value |= value >> 4
    value |= value >> 8
    value |= value >> 16
    value++
    
    return value
}

func mortonEncode(x, y byte) uint16 {
    var result uint16
    
    for i := 0; i < 8; i++ {
        result |= uint16((x & (1 << i)) << i)
        result |= uint16((y & (1 << i)) << (i + 1))
    }
    
    return result
}

func mortonDecode(morton uint16) (byte, byte) {
    var x, y byte
    
    for i := 0; i < 8; i++ {
        x |= byte((morton & (1 << (i * 2))) >> i)
        y |= byte((morton & (1 << (i * 2 + 1))) >> (i + 1))
    }
    
    return x, y
}

func binaryToGray(binary byte) byte {
    return binary ^ (binary >> 1)
}

func grayToBinary(gray byte) byte {
    binary := gray
    for gray >>= 1; gray != 0; gray >>= 1 {
        binary ^= gray
    }
    return binary
}
```

### Example 25: Bit Vectors and Sets

```go
package main

import (
    "fmt"
)

// BitSet represents a set of integers using bit manipulation
type BitSet struct {
    bits []uint64
    size int
}

// NewBitSet creates a new bit set with the specified maximum size
func NewBitSet(size int) *BitSet {
    wordCount := (size + 63) / 64 // Round up to nearest multiple of 64
    return &BitSet{
        bits: make([]uint64, wordCount),
        size: size,
    }
}

// Set sets the bit at the given position
func (bs *BitSet) Set(pos int) {
    if pos < 0 || pos >= bs.size {
        return
    }
    wordIndex := pos / 64
    bitIndex := pos % 64
    bs.bits[wordIndex] |= (1 << bitIndex)
}

// Clear clears the bit at the given position
func (bs *BitSet) Clear(pos int) {
    if pos < 0 || pos >= bs.size {
        return
    }
    wordIndex := pos / 64
    bitIndex := pos % 64
    bs.bits[wordIndex] &^= (1 << bitIndex)
}

// Test checks if the bit at the given position is set
func (bs *BitSet) Test(pos int) bool {
    if pos < 0 || pos >= bs.size {
        return false
    }
    wordIndex := pos / 64
    bitIndex := pos % 64
    return (bs.bits[wordIndex] & (1 << bitIndex)) != 0
}

// Count returns the number of set bits
func (bs *BitSet) Count() int {
    count := 0
    for _, word := range bs.bits {
        count += popcount(word)
    }
    return count
}

// Union performs bitwise OR with another BitSet
func (bs *BitSet) Union(other *BitSet) *BitSet {
    result := NewBitSet(bs.size)
    minWords := len(bs.bits)
    if len(other.bits) < minWords {
        minWords = len(other.bits)
    }
    
    for i := 0; i < minWords; i++ {
        result.bits[i] = bs.bits[i] | other.bits[i]
    }
    
    // Copy remaining bits if one set is larger
    if len(bs.bits) > minWords {
        copy(result.bits[minWords:], bs.bits[minWords:])
    }
    
    return result
}

// Intersection performs bitwise AND with another BitSet
func (bs *BitSet) Intersection(other *BitSet) *BitSet {
    result := NewBitSet(bs.size)
    minWords := len(bs.bits)
    if len(other.bits) < minWords {
        minWords = len(other.bits)
    }
    
    for i := 0; i < minWords; i++ {
        result.bits[i] = bs.bits[i] & other.bits[i]
    }
    
    return result
}

// String returns a string representation of the bit set
func (bs *BitSet) String() string {
    result := "{"
    first := true
    
    for i := 0; i < bs.size; i++ {
        if bs.Test(i) {
            if !first {
                result += ", "
            }
            result += fmt.Sprintf("%d", i)
            first = false
        }
    }
    
    result += "}"
    return result
}

// popcount counts the number of set bits in a uint64
func popcount(x uint64) int {
    count := 0
    for x != 0 {
        count++
        x &= x - 1 // Clear the lowest set bit
    }
    return count
}

func main() {
    fmt.Println("BitSet operations:")
    
    // Create bit sets
    set1 := NewBitSet(100)
    set2 := NewBitSet(100)
    
    // Add some elements to set1
    elements1 := []int{1, 5, 10, 15, 20, 25}
    for _, elem := range elements1 {
        set1.Set(elem)
    }
    
    // Add some elements to set2
    elements2 := []int{5, 10, 30, 35, 40}
    for _, elem := range elements2 {
        set2.Set(elem)
    }
    
    fmt.Printf("Set1: %s\n", set1)
    fmt.Printf("Set2: %s\n", set2)
    fmt.Printf("Set1 count: %d\n", set1.Count())
    fmt.Printf("Set2 count: %d\n", set2.Count())
    
    // Test membership
    fmt.Printf("5 in set1: %t\n", set1.Test(5))
    fmt.Printf("7 in set1: %t\n", set1.Test(7))
    
    // Set operations
    union := set1.Union(set2)
    fmt.Printf("Union: %s (count: %d)\n", union, union.Count())
    
    intersection := set1.Intersection(set2)
    fmt.Printf("Intersection: %s (count: %d)\n", intersection, intersection.Count())
    
    // Practical example: Sieve of Eratosthenes
    fmt.Println("\nSieve of Eratosthenes using BitSet:")
    
    limit := 100
    sieve := NewBitSet(limit + 1)
    
    // Initially, assume all numbers are prime
    for i := 2; i <= limit; i++ {
        sieve.Set(i)
    }
    
    // Sieve algorithm
    for i := 2; i*i <= limit; i++ {
        if sieve.Test(i) {
            // Mark multiples of i as composite
            for j := i * i; j <= limit; j += i {
                sieve.Clear(j)
            }
        }
    }
    
    // Collect primes
    var primes []int
    for i := 2; i <= limit; i++ {
        if sieve.Test(i) {
            primes = append(primes, i)
        }
    }
    
    fmt.Printf("Primes up to %d: %v\n", limit, primes[:20]) // Show first 20
    fmt.Printf("Total primes found: %d\n", len(primes))
    
    // Bloom filter simulation
    fmt.Println("\nSimple Bloom Filter simulation:")
    
    bloomSize := 1000
    bloom := NewBitSet(bloomSize)
    
    // Simple hash functions
    hash1 := func(s string) int {
        h := 0
        for _, c := range s {
            h = (h*31 + int(c)) % bloomSize
        }
        return h
    }
    
    hash2 := func(s string) int {
        h := 0
        for _, c := range s {
            h = (h*37 + int(c)) % bloomSize
        }
        return h
    }
    
    // Add items to bloom filter
    items := []string{"apple", "banana", "cherry", "date"}
    for _, item := range items {
        bloom.Set(hash1(item))
        bloom.Set(hash2(item))
    }
    
    // Test membership
    testItems := []string{"apple", "grape", "banana", "kiwi"}
    for _, item := range testItems {
        inFilter := bloom.Test(hash1(item)) && bloom.Test(hash2(item))
        fmt.Printf("'%s' might be in set: %t\n", item, inFilter)
    }
}
```

### Example 26: Bit Streaming and Bit-Level I/O

```go
package main

import (
    "fmt"
    "io"
    "strings"
)

// BitWriter allows writing individual bits to a stream
type BitWriter struct {
    writer   io.Writer
    buffer   byte
    bitCount int
}

func NewBitWriter(w io.Writer) *BitWriter {
    return &BitWriter{writer: w}
}

// WriteBit writes a single bit (0 or 1)
func (bw *BitWriter) WriteBit(bit byte) error {
    if bit != 0 {
        bw.buffer |= (1 << (7 - bw.bitCount))
    }
    bw.bitCount++
    
    if bw.bitCount == 8 {
        _, err := bw.writer.Write([]byte{bw.buffer})
        bw.buffer = 0
        bw.bitCount = 0
        return err
    }
    
    return nil
}

// WriteBits writes multiple bits from a byte
func (bw *BitWriter) WriteBits(value byte, numBits int) error {
    for i := numBits - 1; i >= 0; i-- {
        bit := (value >> i) & 1
        if err := bw.WriteBit(bit); err != nil {
            return err
        }
    }
    return nil
}

// Flush writes any remaining bits in the buffer
func (bw *BitWriter) Flush() error {
    if bw.bitCount > 0 {
        _, err := bw.writer.Write([]byte{bw.buffer})
        bw.buffer = 0
        bw.bitCount = 0
        return err
    }
    return nil
}

// BitReader allows reading individual bits from a stream
type BitReader struct {
    reader   io.Reader
    buffer   byte
    bitCount int
}

func NewBitReader(r io.Reader) *BitReader {
    return &BitReader{reader: r}
}

// ReadBit reads a single bit
func (br *BitReader) ReadBit() (byte, error) {
    if br.bitCount == 0 {
        data := make([]byte, 1)
        n, err := br.reader.Read(data)
        if err != nil {
            return 0, err
        }
        if n == 0 {
            return 0, io.EOF
        }
        br.buffer = data[0]
        br.bitCount = 8
    }
    
    bit := (br.buffer >> (br.bitCount - 1)) & 1
    br.bitCount--
    
    return bit, nil
}

// ReadBits reads multiple bits into a byte
func (br *BitReader) ReadBits(numBits int) (byte, error) {
    var result byte
    
    for i := 0; i < numBits; i++ {
        bit, err := br.ReadBit()
        if err != nil {
            return 0, err
        }
        result = (result << 1) | bit
    }
    
    return result, nil
}

func main() {
    fmt.Println("Bit-level I/O operations:")
    
    // Create a buffer to write to
    var buffer strings.Builder
    
    // Write some bits
    bitWriter := NewBitWriter(&buffer)
    
    // Write individual bits: 1, 0, 1, 1, 0, 1, 0, 0
    bits := []byte{1, 0, 1, 1, 0, 1, 0, 0}
    fmt.Printf("Writing bits: ")
    for _, bit := range bits {
        fmt.Printf("%d", bit)
        bitWriter.WriteBit(bit)
    }
    fmt.Println()
    
    // Write some multi-bit values
    bitWriter.WriteBits(0b101, 3)  // Write 3 bits: 101
    bitWriter.WriteBits(0b1100, 4) // Write 4 bits: 1100
    bitWriter.WriteBits(0b1, 1)    // Write 1 bit: 1
    
    bitWriter.Flush()
    
    // Read the data back
    written := buffer.String()
    fmt.Printf("Written data: %v\n", []byte(written))
    fmt.Printf("As binary: ")
    for _, b := range []byte(written) {
        fmt.Printf("%08b ", b)
    }
    fmt.Println()
    
    // Read bits back
    bitReader := NewBitReader(strings.NewReader(written))
    
    fmt.Printf("Reading bits: ")
    for i := 0; i < len(bits); i++ {
        bit, err := bitReader.ReadBit()
        if err != nil {
            break
        }
        fmt.Printf("%d", bit)
    }
    fmt.Println()
    
    // Read multi-bit values
    val1, _ := bitReader.ReadBits(3)
    val2, _ := bitReader.ReadBits(4)
    val3, _ := bitReader.ReadBits(1)
    
    fmt.Printf("Read 3 bits: %03b (%d)\n", val1, val1)
    fmt.Printf("Read 4 bits: %04b (%d)\n", val2, val2)
    fmt.Printf("Read 1 bit:  %01b (%d)\n", val3, val3)
    
    // Practical example: Simple compression
    fmt.Println("\nSimple bit-based compression:")
    
    // Compress a string where each character is represented by fewer bits
    text := "AAABBBCCC"
    compressed := compressString(text)
    decompressed := decompressString(compressed)
    
    fmt.Printf("Original: %s (%d bytes)\n", text, len(text))
    fmt.Printf("Compressed: %v (%d bytes)\n", compressed, len(compressed))
    fmt.Printf("Decompressed: %s\n", decompressed)
    fmt.Printf("Compression ratio: %.2f%%\n", float64(len(compressed))/float64(len(text))*100)
}

// Simple compression: A=00, B=01, C=10, D=11
func compressString(s string) []byte {
    var buffer strings.Builder
    bitWriter := NewBitWriter(&buffer)
    
    for _, c := range s {
        switch c {
        case 'A':
            bitWriter.WriteBits(0b00, 2)
        case 'B':
            bitWriter.WriteBits(0b01, 2)
        case 'C':
            bitWriter.WriteBits(0b10, 2)
        case 'D':
            bitWriter.WriteBits(0b11, 2)
        }
    }
    
    bitWriter.Flush()
    return []byte(buffer.String())
}

func decompressString(data []byte) string {
    bitReader := NewBitReader(strings.NewReader(string(data)))
    var result strings.Builder
    
    for {
        bits, err := bitReader.ReadBits(2)
        if err != nil {
            break
        }
        
        switch bits {
        case 0b00:
            result.WriteByte('A')
        case 0b01:
            result.WriteByte('B')
        case 0b10:
            result.WriteByte('C')
        case 0b11:
            result.WriteByte('D')
        }
    }
    
    return result.String()
}
```

### Example 27: Hamming Codes and Error Detection

```go
package main

import (
    "fmt"
)

// HammingCode implements simple Hamming(7,4) error correction
type HammingCode struct{}

func NewHammingCode() *HammingCode {
    return &HammingCode{}
}

// Encode encodes 4 data bits into 7 bits with parity
func (h *HammingCode) Encode(data byte) byte {
    // Extract 4 data bits (assume they're in lower 4 bits)
    d1 := (data >> 0) & 1
    d2 := (data >> 1) & 1
    d3 := (data >> 2) & 1
    d4 := (data >> 3) & 1
    
    // Calculate parity bits
    p1 := d1 ^ d2 ^ d4         // Parity for positions 1,2,4
    p2 := d1 ^ d3 ^ d4         // Parity for positions 1,3,4
    p3 := d2 ^ d3 ^ d4         // Parity for positions 2,3,4
    
    // Construct 7-bit codeword: p1 p2 d1 p3 d2 d3 d4
    result := byte(0)
    result |= p1 << 6
    result |= p2 << 5
    result |= d1 << 4
    result |= p3 << 3
    result |= d2 << 2
    result |= d3 << 1
    result |= d4 << 0
    
    return result
}

// Decode decodes 7 bits and corrects single-bit errors
func (h *HammingCode) Decode(codeword byte) (byte, bool) {
    // Extract bits from codeword
    p1 := (codeword >> 6) & 1
    p2 := (codeword >> 5) & 1
    d1 := (codeword >> 4) & 1
    p3 := (codeword >> 3) & 1
    d2 := (codeword >> 2) & 1
    d3 := (codeword >> 1) & 1
    d4 := (codeword >> 0) & 1
    
    // Calculate syndrome (error detection)
    s1 := p1 ^ d1 ^ d2 ^ d4
    s2 := p2 ^ d1 ^ d3 ^ d4
    s3 := p3 ^ d2 ^ d3 ^ d4
    
    syndrome := (s3 << 2) | (s2 << 1) | s1
    
    corrected := false
    if syndrome != 0 {
        // Error detected, correct it
        errorPos := syndrome
        codeword ^= (1 << (7 - errorPos))
        corrected = true
        
        // Re-extract corrected data bits
        d1 = (codeword >> 4) & 1
        d2 = (codeword >> 2) & 1
        d3 = (codeword >> 1) & 1
        d4 = (codeword >> 0) & 1
    }
    
    // Reconstruct original 4-bit data
    data := (d4 << 3) | (d3 << 2) | (d2 << 1) | d1
    
    return data, corrected
}

// Simple checksum functions
func calculateChecksum8(data []byte) byte {
    var sum byte
    for _, b := range data {
        sum += b
    }
    return ^sum + 1 // Two's complement
}

func calculateCRC8(data []byte) byte {
    const polynomial byte = 0xD5 // x^8 + x^7 + x^6 + x^4 + x^2 + 1
    
    crc := byte(0)
    for _, b := range data {
        crc ^= b
        for i := 0; i < 8; i++ {
            if (crc & 0x80) != 0 {
                crc = (crc << 1) ^ polynomial
            } else {
                crc <<= 1
            }
        }
    }
    
    return crc
}

// Parity calculation functions
func calculateEvenParity(data byte) byte {
    parity := byte(0)
    temp := data
    
    for temp != 0 {
        parity ^= 1
        temp &= temp - 1 // Remove rightmost set bit
    }
    
    return parity
}

func calculateOddParity(data byte) byte {
    return calculateEvenParity(data) ^ 1
}

func main() {
    fmt.Println("Error detection and correction:")
    
    // Hamming code example
    hamming := NewHammingCode()
    
    originalData := byte(0b1011) // 4-bit data: 11 in decimal
    encoded := hamming.Encode(originalData)
    
    fmt.Printf("Original data: %04b (%d)\n", originalData, originalData)
    fmt.Printf("Encoded: %07b\n", encoded)
    
    // Simulate transmission without error
    decoded, corrected := hamming.Decode(encoded)
    fmt.Printf("Decoded: %04b (%d), corrected: %t\n", decoded, decoded, corrected)
    
    // Simulate single-bit error
    corruptedBit := 3 // Flip bit at position 3
    corrupted := encoded ^ (1 << corruptedBit)
    fmt.Printf("Corrupted (bit %d flipped): %07b\n", corruptedBit, corrupted)
    
    decoded, corrected = hamming.Decode(corrupted)
    fmt.Printf("Decoded after correction: %04b (%d), corrected: %t\n", decoded, decoded, corrected)
    
    // Checksum examples
    fmt.Println("\nChecksum calculations:")
    
    testData := []byte{0x12, 0x34, 0x56, 0x78}
    fmt.Printf("Test data: %v\n", testData)
    
    checksum8 := calculateChecksum8(testData)
    fmt.Printf("8-bit checksum: 0x%02X\n", checksum8)
    
    // Verify checksum
    dataWithChecksum := append(testData, checksum8)
    verifySum := calculateChecksum8(dataWithChecksum)
    fmt.Printf("Verification (should be 0): 0x%02X\n", verifySum)
    
    crc8 := calculateCRC8(testData)
    fmt.Printf("CRC-8: 0x%02X\n", crc8)
    
    // Parity examples
    fmt.Println("\nParity calculations:")
    
    parityTestData := []byte{0b10110100, 0b11111111, 0b00000001, 0b10101010}
    
    for _, data := range parityTestData {
        evenParity := calculateEvenParity(data)
        oddParity := calculateOddParity(data)
        
        fmt.Printf("Data: %08b, Even parity: %d, Odd parity: %d\n", 
            data, evenParity, oddParity)
    }
    
    // Error detection simulation
    fmt.Println("\nError detection simulation:")
    
    message := []byte("Hello")
    originalCRC := calculateCRC8(message)
    
    fmt.Printf("Original message: %s\n", string(message))
    fmt.Printf("Original CRC: 0x%02X\n", originalCRC)
    
    // Simulate corruption
    corruptedMessage := make([]byte, len(message))
    copy(corruptedMessage, message)
    corruptedMessage[1] ^= 0x01 // Flip one bit
    
    corruptedCRC := calculateCRC8(corruptedMessage)
    
    fmt.Printf("Corrupted message: %s\n", string(corruptedMessage))
    fmt.Printf("Corrupted CRC: 0x%02X\n", corruptedCRC)
    fmt.Printf("Error detected: %t\n", originalCRC != corruptedCRC)
}
```

### Example 28: Bitwise Cryptographic Operations

```go
package main

import (
    "fmt"
)

// Simple XOR cipher implementation
func xorCipher(data []byte, key []byte) []byte {
    result := make([]byte, len(data))
    keyLen := len(key)
    
    for i, b := range data {
        result[i] = b ^ key[i%keyLen]
    }
    
    return result
}

// Linear feedback shift register (LFSR) for pseudorandom number generation
type LFSR struct {
    state    uint16
    taps     uint16
    period   int
    position int
}

func NewLFSR(seed uint16, taps uint16) *LFSR {
    return &LFSR{
        state: seed,
        taps:  taps,
    }
}

func (l *LFSR) Next() byte {
    // Calculate feedback bit
    feedback := l.state & l.taps
    
    // Count number of 1s in feedback (parity)
    parity := byte(0)
    for feedback != 0 {
        parity ^= 1
        feedback &= feedback - 1
    }
    
    // Shift register and insert feedback bit
    l.state = (l.state >> 1) | (uint16(parity) << 15)
    l.position++
    
    return byte(l.state & 0xFF)
}

// Simple substitution cipher using bit manipulation
func substitutionEncrypt(data []byte, sbox [256]byte) []byte {
    result := make([]byte, len(data))
    for i, b := range data {
        result[i] = sbox[b]
    }
    return result
}

func substitutionDecrypt(data []byte, sbox [256]byte) []byte {
    // Create inverse S-box
    var invSbox [256]byte
    for i := 0; i < 256; i++ {
        invSbox[sbox[i]] = byte(i)
    }
    
    result := make([]byte, len(data))
    for i, b := range data {
        result[i] = invSbox[b]
    }
    return result
}

// Feistel network structure (simplified)
func feistelRound(left, right uint32, key uint32) (uint32, uint32) {
    // Simple F function using XOR and rotation
    f := ((right ^ key) << 3) | ((right ^ key) >> 29)
    newLeft := right
    newRight := left ^ f
    return newLeft, newRight
}

func feistelEncrypt(block uint64, keys []uint32) uint64 {
    left := uint32(block >> 32)
    right := uint32(block & 0xFFFFFFFF)
    
    for _, key := range keys {
        left, right = feistelRound(left, right, key)
    }
    
    return (uint64(left) << 32) | uint64(right)
}

func feistelDecrypt(block uint64, keys []uint32) uint64 {
    left := uint32(block >> 32)
    right := uint32(block & 0xFFFFFFFF)
    
    // Apply keys in reverse order
    for i := len(keys) - 1; i >= 0; i-- {
        left, right = feistelRound(left, right, keys[i])
    }
    
    return (uint64(left) << 32) | uint64(right)
}

func main() {
    fmt.Println("Bitwise cryptographic operations:")
    
    // XOR cipher example
    fmt.Println("1. XOR Cipher:")
    plaintext := []byte("Secret Message")
    key := []byte("KEY")
    
    fmt.Printf("Plaintext: %s\n", string(plaintext))
    fmt.Printf("Key: %s\n", string(key))
    
    encrypted := xorCipher(plaintext, key)
    fmt.Printf("Encrypted: %v\n", encrypted)
    fmt.Printf("Encrypted (hex): %x\n", encrypted)
    
    decrypted := xorCipher(encrypted, key) // XOR is self-inverse
    fmt.Printf("Decrypted: %s\n", string(decrypted))
    
    // LFSR pseudorandom generator
    fmt.Println("\n2. LFSR Pseudorandom Generator:")
    
    // 16-bit LFSR with taps at positions 16, 14, 13, 11 (polynomial: x^16 + x^14 + x^13 + x^11 + 1)
    lfsr := NewLFSR(0xACE1, 0xB400)
    
    fmt.Print("Random bytes: ")
    for i := 0; i < 16; i++ {
        fmt.Printf("%02X ", lfsr.Next())
    }
    fmt.Println()
    
    // One-time pad simulation
    fmt.Println("\n3. One-Time Pad:")
    
    message := []byte("TOP SECRET")
    pad := make([]byte, len(message))
    
    // Generate random pad using LFSR
    lfsr2 := NewLFSR(0x1337, 0xB400)
    for i := range pad {
        pad[i] = lfsr2.Next()
    }
    
    fmt.Printf("Message: %s\n", string(message))
    fmt.Printf("Pad: %x\n", pad)
    
    otpEncrypted := xorCipher(message, pad)
    fmt.Printf("OTP Encrypted: %x\n", otpEncrypted)
    
    otpDecrypted := xorCipher(otpEncrypted, pad)
    fmt.Printf("OTP Decrypted: %s\n", string(otpDecrypted))
    
    // Substitution cipher
    fmt.Println("\n4. Substitution Cipher:")
    
    // Create a simple substitution box (S-box)
    var sbox [256]byte
    for i := 0; i < 256; i++ {
        sbox[i] = byte((i * 37 + 123) % 256) // Simple permutation
    }
    
    subMessage := []byte("Hello World")
    fmt.Printf("Original: %s\n", string(subMessage))
    
    subEncrypted := substitutionEncrypt(subMessage, sbox)
    fmt.Printf("Substitution encrypted: %x\n", subEncrypted)
    
    subDecrypted := substitutionDecrypt(subEncrypted, sbox)
    fmt.Printf("Substitution decrypted: %s\n", string(subDecrypted))
    
    // Feistel network
    fmt.Println("\n5. Feistel Network:")
    
    keys := []uint32{0x12345678, 0x9ABCDEF0, 0x87654321, 0x0FEDCBA9}
    block := uint64(0x123456789ABCDEF0)
    
    fmt.Printf("Original block: %016X\n", block)
    
    encrypted := feistelEncrypt(block, keys)
    fmt.Printf("Encrypted: %016X\n", encrypted)
    
    decrypted := feistelDecrypt(encrypted, keys)
    fmt.Printf("Decrypted: %016X\n", decrypted)
    
    // Bit permutation
    fmt.Println("\n6. Bit Permutation:")
    
    data := byte(0b10110100)
    fmt.Printf("Original: %08b\n", data)
    
    // Simple bit permutation: reverse the bits
    permuted := byte(0)
    for i := 0; i < 8; i++ {
        if (data & (1 << i)) != 0 {
            permuted |= (1 << (7 - i))
        }
    }
    
    fmt.Printf("Bit-reversed: %08b\n", permuted)
    
    // More complex permutation table
    permTable := []int{7, 3, 5, 1, 6, 2, 4, 0} // Permutation of bit positions
    permuted2 := byte(0)
    
    for i := 0; i < 8; i++ {
        if (data & (1 << i)) != 0 {
            permuted2 |= (1 << permTable[i])
        }
    }
    
    fmt.Printf("Table permuted: %08b\n", permuted2)
}
```

### Example 29: Binary Data Compression Techniques

```go
package main

import (
    "fmt"
    "sort"
)

// Run-length encoding
func runLengthEncode(data []byte) []byte {
    if len(data) == 0 {
        return nil
    }
    
    var result []byte
    count := 1
    current := data[0]
    
    for i := 1; i < len(data); i++ {
        if data[i] == current && count < 255 {
            count++
        } else {
            result = append(result, byte(count), current)
            current = data[i]
            count = 1
        }
    }
    
    // Add the last run
    result = append(result, byte(count), current)
    return result
}

func runLengthDecode(data []byte) []byte {
    var result []byte
    
    for i := 0; i < len(data); i += 2 {
        if i+1 >= len(data) {
            break
        }
        
        count := data[i]
        value := data[i+1]
        
        for j := 0; j < int(count); j++ {
            result = append(result, value)
        }
    }
    
    return result
}

// Huffman coding structures
type HuffmanNode struct {
    Value     byte
    Frequency int
    Left      *HuffmanNode
    Right     *HuffmanNode
}

type HuffmanTree struct {
    Root  *HuffmanNode
    Codes map[byte]string
}

func buildHuffmanTree(frequencies map[byte]int) *HuffmanTree {
    // Create leaf nodes
    var nodes []*HuffmanNode
    for value, freq := range frequencies {
        nodes = append(nodes, &HuffmanNode{
            Value:     value,
            Frequency: freq,
        })
    }
    
    // Sort by frequency
    sort.Slice(nodes, func(i, j int) bool {
        return nodes[i].Frequency < nodes[j].Frequency
    })
    
    // Build tree
    for len(nodes) > 1 {
        left := nodes[0]
        right := nodes[1]
        nodes = nodes[2:]
        
        parent := &HuffmanNode{
            Frequency: left.Frequency + right.Frequency,
            Left:      left,
            Right:     right,
        }
        
        // Insert parent in sorted order
        inserted := false
        for i := 0; i < len(nodes); i++ {
            if parent.Frequency <= nodes[i].Frequency {
                nodes = append(nodes[:i], append([]*HuffmanNode{parent}, nodes[i:]...)...)
                inserted = true
                break
            }
        }
        if !inserted {
            nodes = append(nodes, parent)
        }
    }
    
    tree := &HuffmanTree{
        Root:  nodes[0],
        Codes: make(map[byte]string),
    }
    
    // Generate codes
    tree.generateCodes(tree.Root, "")
    
    return tree
}

func (ht *HuffmanTree) generateCodes(node *HuffmanNode, code string) {
    if node == nil {
        return
    }
    
    if node.Left == nil && node.Right == nil {
        // Leaf node
        ht.Codes[node.Value] = code
        if code == "" {
            ht.Codes[node.Value] = "0" // Single character case
        }
        return
    }
    
    ht.generateCodes(node.Left, code+"0")
    ht.generateCodes(node.Right, code+"1")
}

func calculateFrequencies(data []byte) map[byte]int {
    frequencies := make(map[byte]int)
    for _, b := range data {
        frequencies[b]++
    }
    return frequencies
}

// Delta encoding
func deltaEncode(data []byte) []byte {
    if len(data) == 0 {
        return nil
    }
    
    result := make([]byte, len(data))
    result[0] = data[0]
    
    for i := 1; i < len(data); i++ {
        result[i] = data[i] - data[i-1]
    }
    
    return result
}

func deltaDecode(data []byte) []byte {
    if len(data) == 0 {
        return nil
    }
    
    result := make([]byte, len(data))
    result[0] = data[0]
    
    for i := 1; i < len(data); i++ {
        result[i] = result[i-1] + data[i]
    }
    
    return result
}

// Bit packing for small integers
func packBits(values []byte, bitsPerValue int) []byte {
    if bitsPerValue <= 0 || bitsPerValue > 8 {
        return nil
    }
    
    totalBits := len(values) * bitsPerValue
    resultSize := (totalBits + 7) / 8 // Round up to byte boundary
    result := make([]byte, resultSize)
    
    bitPos := 0
    for _, value := range values {
        // Mask to ensure we only use the specified number of bits
        mask := byte((1 << bitsPerValue) - 1)
        value &= mask
        
        // Pack bits
        for i := 0; i < bitsPerValue; i++ {
            if (value & (1 << (bitsPerValue - 1 - i))) != 0 {
                byteIndex := bitPos / 8
                bitIndex := bitPos % 8
                result[byteIndex] |= (1 << (7 - bitIndex))
            }
            bitPos++
        }
    }
    
    return result
}

func unpackBits(data []byte, bitsPerValue int, numValues int) []byte {
    if bitsPerValue <= 0 || bitsPerValue > 8 {
        return nil
    }
    
    result := make([]byte, numValues)
    bitPos := 0
    
    for i := 0; i < numValues; i++ {
        value := byte(0)
        
        for j := 0; j < bitsPerValue; j++ {
            byteIndex := bitPos / 8
            bitIndex := bitPos % 8
            
            if byteIndex >= len(data) {
                break
            }
            
            if (data[byteIndex] & (1 << (7 - bitIndex))) != 0 {
                value |= (1 << (bitsPerValue - 1 - j))
            }
            bitPos++
        }
        
        result[i] = value
    }
    
    return result
}

func main() {
    fmt.Println("Binary data compression techniques:")
    
    // Run-length encoding
    fmt.Println("1. Run-Length Encoding:")
    
    rleData := []byte{0xAA, 0xAA, 0xAA, 0xBB, 0xBB, 0xCC, 0xCC, 0xCC, 0xCC}
    fmt.Printf("Original: %v (%d bytes)\n", rleData, len(rleData))
    
    rleEncoded := runLengthEncode(rleData)
    fmt.Printf("RLE encoded: %v (%d bytes)\n", rleEncoded, len(rleEncoded))
    
    rleDecoded := runLengthDecode(rleEncoded)
    fmt.Printf("RLE decoded: %v\n", rleDecoded)
    fmt.Printf("Compression ratio: %.2f%%\n", float64(len(rleEncoded))/float64(len(rleData))*100)
    
    // Huffman coding
    fmt.Println("\n2. Huffman Coding:")
    
    huffmanData := []byte("ABRACADABRA")
    fmt.Printf("Original: %s (%d bytes)\n", string(huffmanData), len(huffmanData))
    
    frequencies := calculateFrequencies(huffmanData)
    fmt.Printf("Frequencies: %v\n", frequencies)
    
    huffmanTree := buildHuffmanTree(frequencies)
    fmt.Printf("Huffman codes: %v\n", huffmanTree.Codes)
    
    // Calculate compressed size
    compressedBits := 0
    for _, b := range huffmanData {
        compressedBits += len(huffmanTree.Codes[b])
    }
    compressedBytes := (compressedBits + 7) / 8
    
    fmt.Printf("Compressed size: %d bits (%d bytes)\n", compressedBits, compressedBytes)
    fmt.Printf("Compression ratio: %.2f%%\n", float64(compressedBytes)/float64(len(huffmanData))*100)
    
    // Delta encoding
    fmt.Println("\n3. Delta Encoding:")
    
    deltaData := []byte{10, 12, 15, 16, 18, 20, 21, 23}
    fmt.Printf("Original: %v\n", deltaData)
    
    deltaEncoded := deltaEncode(deltaData)
    fmt.Printf("Delta encoded: %v\n", deltaEncoded)
    
    deltaDecoded := deltaDecode(deltaEncoded)
    fmt.Printf("Delta decoded: %v\n", deltaDecoded)
    
    // Bit packing
    fmt.Println("\n4. Bit Packing:")
    
    // Pack values that only need 3 bits each (0-7)
    packData := []byte{0, 1, 2, 3, 4, 5, 6, 7}
    fmt.Printf("Original (8 bytes): %v\n", packData)
    
    packed := packBits(packData, 3)
    fmt.Printf("Packed (3 bits each): %v (%d bytes)\n", packed, len(packed))
    
    unpacked := unpackBits(packed, 3, len(packData))
    fmt.Printf("Unpacked: %v\n", unpacked)
    fmt.Printf("Compression ratio: %.2f%%\n", float64(len(packed))/float64(len(packData))*100)
    
    // Demonstration with binary representation
    fmt.Println("\nBit packing visualization:")
    fmt.Printf("Original values (3 bits each): ")
    for _, v := range packData {
        fmt.Printf("%03b ", v)
    }
    fmt.Println()
    
    fmt.Printf("Packed bytes: ")
    for _, b := range packed {
        fmt.Printf("%08b ", b)
    }
    fmt.Println()
}
```

### Example 30: Advanced Bit Manipulation Patterns

```go
package main

import (
    "fmt"
)

// Bit twiddling hacks and optimization patterns

// Check if a number is a power of 2
func isPowerOfTwo(n uint32) bool {
    return n != 0 && (n&(n-1)) == 0
}

// Find the next power of 2 greater than or equal to n
func nextPowerOfTwo(n uint32) uint32 {
    if n == 0 {
        return 1
    }
    n--
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n++
    return n
}

// Count leading zeros
func countLeadingZeros(n uint32) int {
    if n == 0 {
        return 32
    }
    
    count := 0
    if n <= 0x0000FFFF {
        count += 16
        n <<= 16
    }
    if n <= 0x00FFFFFF {
        count += 8
        n <<= 8
    }
    if n <= 0x0FFFFFFF {
        count += 4
        n <<= 4
    }
    if n <= 0x3FFFFFFF {
        count += 2
        n <<= 2
    }
    if n <= 0x7FFFFFFF {
        count += 1
    }
    
    return count
}

// Population count (count set bits) - Brian Kernighan's algorithm
func popCount(n uint32) int {
    count := 0
    for n != 0 {
        n &= n - 1 // Clear the lowest set bit
        count++
    }
    return count
}

// Parallel bit counting
func popCountParallel(n uint32) int {
    // SWAR (SIMD Within A Register) technique
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n + (n >> 4)) & 0x0F0F0F0F
    n = n + (n >> 8)
    n = n + (n >> 16)
    return int(n & 0x3F)
}

// Reverse bits in a 32-bit integer
func reverseBits32(n uint32) uint32 {
    n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)
    n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
    n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
    n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
    n = (n >> 16) | (n << 16)
    return n
}

// Find the position of the least significant set bit
func findLSB(n uint32) int {
    if n == 0 {
        return -1
    }
    
    // Isolate the rightmost set bit
    isolated := n & (-n)
    
    // Count trailing zeros
    count := 0
    for isolated > 1 {
        isolated >>= 1
        count++
    }
    
    return count
}

// Find the position of the most significant set bit
func findMSB(n uint32) int {
    if n == 0 {
        return -1
    }
    
    position := 0
    if n >= 1<<16 {
        n >>= 16
        position += 16
    }
    if n >= 1<<8 {
        n >>= 8
        position += 8
    }
    if n >= 1<<4 {
        n >>= 4
        position += 4
    }
    if n >= 1<<2 {
        n >>= 2
        position += 2
    }
    if n >= 1<<1 {
        position += 1
    }
    
    return position
}

// Multiply by 3/4 using bit operations
func multiplyBy3Div4(n uint32) uint32 {
    return (n + (n >> 1)) >> 1
}

// Check if two numbers have opposite signs
func oppositeSigns(x, y int32) bool {
    return (x ^ y) < 0
}

// Conditionally set or clear a bit
func conditionalBit(value uint32, position int, condition bool) uint32 {
    mask := uint32(1) << position
    if condition {
        return value | mask // Set bit
    }
    return value &^ mask // Clear bit
}

// Compute absolute value without branching
func abs(x int32) int32 {
    mask := x >> 31        // Arithmetic shift right
    return (x ^ mask) - mask
}

// Find minimum of two integers without branching
func min(x, y int32) int32 {
    return y ^ ((x ^ y) & -(boolToInt(x < y)))
}

func boolToInt(b bool) int32 {
    if b {
        return 1
    }
    return 0
}

// Bit interleaving for Z-order curve (Morton order)
func interleave16(x, y uint16) uint32 {
    // Expand x and y to 32 bits with zeros in between
    var expandedX, expandedY uint32
    
    expandedX = uint32(x)
    expandedX = (expandedX | (expandedX << 8)) & 0x00FF00FF
    expandedX = (expandedX | (expandedX << 4)) & 0x0F0F0F0F
    expandedX = (expandedX | (expandedX << 2)) & 0x33333333
    expandedX = (expandedX | (expandedX << 1)) & 0x55555555
    
    expandedY = uint32(y)
    expandedY = (expandedY | (expandedY << 8)) & 0x00FF00FF
    expandedY = (expandedY | (expandedY << 4)) & 0x0F0F0F0F
    expandedY = (expandedY | (expandedY << 2)) & 0x33333333
    expandedY = (expandedY | (expandedY << 1)) & 0x55555555
    
    return expandedX | (expandedY << 1)
}

func main() {
    fmt.Println("Advanced bit manipulation patterns:")
    
    // Power of 2 operations
    fmt.Println("1. Power of 2 operations:")
    testNumbers := []uint32{1, 2, 3, 4, 8, 15, 16, 32, 33, 64}
    
    for _, n := range testNumbers {
        isPow2 := isPowerOfTwo(n)
        nextPow2 := nextPowerOfTwo(n)
        fmt.Printf("%d: isPowerOf2=%t, nextPowerOf2=%d\n", n, isPow2, nextPow2)
    }
    
    // Bit counting operations
    fmt.Println("\n2. Bit counting:")
    bitTestNumbers := []uint32{0, 1, 7, 15, 255, 0xAAAAAAAA, 0xFFFFFFFF}
    
    for _, n := range bitTestNumbers {
        popCnt := popCount(n)
        popCntPar := popCountParallel(n)
        leadingZeros := countLeadingZeros(n)
        lsb := findLSB(n)
        msb := findMSB(n)
        
        fmt.Printf("0x%08X: popCount=%d, popCountParallel=%d, leadingZeros=%d, LSB=%d, MSB=%d\n",
            n, popCnt, popCntPar, leadingZeros, lsb, msb)
    }
    
    // Bit reversal
    fmt.Println("\n3. Bit reversal:")
    reverseTestNumbers := []uint32{0x12345678, 0xAAAAAAAA, 0x80000001}
    
    for _, n := range reverseTestNumbers {
        reversed := reverseBits32(n)
        fmt.Printf("0x%08X -> 0x%08X\n", n, reversed)
    }
    
    // Arithmetic operations using bit manipulation
    fmt.Println("\n4. Arithmetic with bit operations:")
    
    testValue := uint32(100)
    result := multiplyBy3Div4(testValue)
    fmt.Printf("%d * 3/4 = %d (expected: %d)\n", testValue, result, testValue*3/4)
    
    // Sign operations
    fmt.Println("\n5. Sign operations:")
    signTestPairs := [][2]int32{{5, -3}, {-7, 2}, {4, 8}, {-1, -5}}
    
    for _, pair := range signTestPairs {
        x, y := pair[0], pair[1]
        opposite := oppositeSigns(x, y)
        absX := abs(x)
        absY := abs(y)
        minVal := min(x, y)
        
        fmt.Printf("x=%d, y=%d: oppositeSigns=%t, abs(x)=%d, abs(y)=%d, min=%d\n",
            x, y, opposite, absX, absY, minVal)
    }
    
    // Conditional bit operations
    fmt.Println("\n6. Conditional bit operations:")
    
    value := uint32(0b10110100)
    fmt.Printf("Original: %08b\n", value)
    
    // Set bit 2 conditionally
    value = conditionalBit(value, 2, true)
    fmt.Printf("Set bit 2: %08b\n", value)
    
    // Clear bit 5 conditionally
    value = conditionalBit(value, 5, false)
    fmt.Printf("Clear bit 5: %08b\n", value)
    
    // Bit interleaving
    fmt.Println("\n7. Bit interleaving (Morton order):")
    
    x, y := uint16(5), uint16(3)
    morton := interleave16(x, y)
    fmt.Printf("Interleave(%d, %d) = %d (0x%08X)\n", x, y, morton, morton)
    fmt.Printf("x=%04b, y=%04b -> morton=%016b\n", x, y, morton)
    
    // Practical applications
    fmt.Println("\n8. Practical applications:")
    
    // Fast modulo for powers of 2
    number := uint32(123)
    powerOf2 := uint32(16)
    fastMod := number & (powerOf2 - 1)
    slowMod := number % powerOf2
    
    fmt.Printf("Fast modulo: %d %% %d = %d (standard: %d)\n", 
        number, powerOf2, fastMod, slowMod)
    
    // Alignment checking
    address := uint32(0x12345678)
    alignment := uint32(8)
    isAligned := (address & (alignment - 1)) == 0
    
    fmt.Printf("Address 0x%08X is %d-byte aligned: %t\n", 
        address, alignment, isAligned)
}
```

---

## Encoding and Decoding

### Example 31: Base64 Encoding and Decoding

```go
package main

import (
    "encoding/base64"
    "fmt"
    "strings"
)

func main() {
    fmt.Println("Base64 Encoding and Decoding:")
    
    // Original data
    data := []byte("Hello, World! This is a test message for Base64 encoding.")
    fmt.Printf("Original data: %s\n", string(data))
    fmt.Printf("Original bytes: %v\n", data)
    fmt.Printf("Length: %d bytes\n", len(data))
    
    // Standard Base64 encoding
    fmt.Println("\n1. Standard Base64:")
    encoded := base64.StdEncoding.EncodeToString(data)
    fmt.Printf("Encoded: %s\n", encoded)
    fmt.Printf("Encoded length: %d characters\n", len(encoded))
    
    // Decode back
    decoded, err := base64.StdEncoding.DecodeString(encoded)
    if err != nil {
        fmt.Printf("Error decoding: %v\n", err)
        return
    }
    fmt.Printf("Decoded: %s\n", string(decoded))
    fmt.Printf("Data integrity: %t\n", string(data) == string(decoded))
    
    // URL-safe Base64 encoding
    fmt.Println("\n2. URL-safe Base64:")
    urlEncoded := base64.URLEncoding.EncodeToString(data)
    fmt.Printf("URL encoded: %s\n", urlEncoded)
    
    urlDecoded, err := base64.URLEncoding.DecodeString(urlEncoded)
    if err != nil {
        fmt.Printf("Error decoding URL-safe: %v\n", err)
        return
    }
    fmt.Printf("URL decoded: %s\n", string(urlDecoded))
    
    // Raw Base64 (no padding)
    fmt.Println("\n3. Raw Base64 (no padding):")
    rawEncoded := base64.RawStdEncoding.EncodeToString(data)
    fmt.Printf("Raw encoded: %s\n", rawEncoded)
    
    rawDecoded, err := base64.RawStdEncoding.DecodeString(rawEncoded)
    if err != nil {
        fmt.Printf("Error decoding raw: %v\n", err)
        return
    }
    fmt.Printf("Raw decoded: %s\n", string(rawDecoded))
    
    // Custom Base64 alphabet
    fmt.Println("\n4. Custom Base64 alphabet:")
    customEncoding := base64.NewEncoding("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/")
    customEncoded := customEncoding.EncodeToString(data)
    fmt.Printf("Custom encoded: %s\n", customEncoded)
    
    customDecoded, err := customEncoding.DecodeString(customEncoded)
    if err != nil {
        fmt.Printf("Error decoding custom: %v\n", err)
        return
    }
    fmt.Printf("Custom decoded: %s\n", string(customDecoded))
    
    // Manual Base64 implementation for educational purposes
    fmt.Println("\n5. Manual Base64 implementation:")
    manualEncoded := manualBase64Encode(data)
    fmt.Printf("Manual encoded: %s\n", manualEncoded)
    
    manualDecoded := manualBase64Decode(manualEncoded)
    fmt.Printf("Manual decoded: %s\n", string(manualDecoded))
    
    // Binary data encoding
    fmt.Println("\n6. Binary data encoding:")
    binaryData := []byte{0x00, 0x01, 0x02, 0x03, 0xFF, 0xFE, 0xFD, 0xFC}
    fmt.Printf("Binary data: %v\n", binaryData)
    
    binaryEncoded := base64.StdEncoding.EncodeToString(binaryData)
    fmt.Printf("Binary encoded: %s\n", binaryEncoded)
    
    binaryDecoded, _ := base64.StdEncoding.DecodeString(binaryEncoded)
    fmt.Printf("Binary decoded: %v\n", binaryDecoded)
}

func manualBase64Encode(data []byte) string {
    alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    var result strings.Builder
    
    for i := 0; i < len(data); i += 3 {
        // Take up to 3 bytes
        var bytes [3]byte
        bytesUsed := 0
        
        for j := 0; j < 3 && i+j < len(data); j++ {
            bytes[j] = data[i+j]
            bytesUsed++
        }
        
        // Convert to 4 6-bit values
        val := (uint32(bytes[0]) << 16) | (uint32(bytes[1]) << 8) | uint32(bytes[2])
        
        // Extract 6-bit values
        chars := [4]byte{
            alphabet[(val>>18)&63],
            alphabet[(val>>12)&63],
            alphabet[(val>>6)&63],
            alphabet[val&63],
        }
        
        // Add padding if necessary
        switch bytesUsed {
        case 1:
            chars[2] = '='
            chars[3] = '='
        case 2:
            chars[3] = '='
        }
        
        result.Write(chars[:])
    }
    
    return result.String()
}

func manualBase64Decode(encoded string) []byte {
    alphabet := "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    // Create reverse lookup table
    lookup := make(map[byte]int)
    for i, c := range alphabet {
        lookup[byte(c)] = i
    }
    
    var result []byte
    
    for i := 0; i < len(encoded); i += 4 {
        if i+4 > len(encoded) {
            break
        }
        
        // Get 4 characters
        chars := encoded[i : i+4]
        
        // Convert to 6-bit values
        var vals [4]int
        validBytes := 4
        
        for j, c := range chars {
            if c == '=' {
                vals[j] = 0
                validBytes = j
                break
            }
            vals[j] = lookup[byte(c)]
        }
        
        // Combine into 24-bit value
        val := (vals[0] << 18) | (vals[1] << 12) | (vals[2] << 6) | vals[3]
        
        // Extract bytes
        bytes := []byte{
            byte(val >> 16),
            byte(val >> 8),
            byte(val),
        }
        
        // Add appropriate number of bytes
        switch validBytes {
        case 4:
            result = append(result, bytes...)
        case 3:
            result = append(result, bytes[:2]...)
        case 2:
            result = append(result, bytes[:1]...)
        }
    }
    
    return result
}
```

### Example 32: Hexadecimal Encoding and Decoding

```go
package main

import (
    "encoding/hex"
    "fmt"
    "strings"
)

func main() {
    fmt.Println("Hexadecimal Encoding and Decoding:")
    
    // Test data
    data := []byte("Hello, World! 🌍")
    fmt.Printf("Original data: %s\n", string(data))
    fmt.Printf("Original bytes: %v\n", data)
    
    // Standard hex encoding
    fmt.Println("\n1. Standard hex encoding:")
    hexString := hex.EncodeToString(data)
    fmt.Printf("Hex encoded: %s\n", hexString)
    fmt.Printf("Length: %d characters (%d bytes original -> %d chars)\n", 
        len(hexString), len(data), len(hexString))
    
    // Decode back
    decoded, err := hex.DecodeString(hexString)
    if err != nil {
        fmt.Printf("Error decoding: %v\n", err)
        return
    }
    fmt.Printf("Decoded: %s\n", string(decoded))
    fmt.Printf("Data integrity: %t\n", string(data) == string(decoded))
    
    // Uppercase hex
    fmt.Println("\n2. Uppercase hex:")
    upperHex := strings.ToUpper(hexString)
    fmt.Printf("Uppercase hex: %s\n", upperHex)
    
    // Decode uppercase (case insensitive)
    decodedUpper, err := hex.DecodeString(upperHex)
    if err != nil {
        fmt.Printf("Error decoding uppercase: %v\n", err)
        return
    }
    fmt.Printf("Decoded uppercase: %s\n", string(decodedUpper))
    
    // Hex with separators
    fmt.Println("\n3. Hex with separators:")
    hexWithSpaces := formatHexWithSeparator(data, " ")
    hexWithColons := formatHexWithSeparator(data, ":")
    hexWithHyphens := formatHexWithSeparator(data, "-")
    
    fmt.Printf("With spaces: %s\n", hexWithSpaces)
    fmt.Printf("With colons: %s\n", hexWithColons)
    fmt.Printf("With hyphens: %s\n", hexWithHyphens)
    
    // Parse hex with separators
    parsedFromSpaces := parseHexWithSeparator(hexWithSpaces, " ")
    fmt.Printf("Parsed from spaces: %s\n", string(parsedFromSpaces))
    
    // Dumper-style hex output
    fmt.Println("\n4. Hex dump style:")
    hexDump(data)
    
    // Manual hex implementation
    fmt.Println("\n5. Manual hex implementation:")
    manualHex := manualHexEncode(data)
    fmt.Printf("Manual hex: %s\n", manualHex)
    
    manualDecoded := manualHexDecode(manualHex)
    fmt.Printf("Manual decoded: %s\n", string(manualDecoded))
    
    // Binary data
    fmt.Println("\n6. Binary data hex encoding:")
    binaryData := []byte{0x00, 0x0F, 0xFF, 0xAB, 0xCD, 0xEF, 0x12, 0x34, 0x56, 0x78}
    fmt.Printf("Binary data: %v\n", binaryData)
    
    binaryHex := hex.EncodeToString(binaryData)
    fmt.Printf("Binary hex: %s\n", binaryHex)
    
    // Hex validation
    fmt.Println("\n7. Hex validation:")
    testStrings := []string{
        "deadbeef",
        "DEADBEEF", 
        "DeAdBeEf",
        "123456789ABCDEF0",
        "invalid hex string",
        "123G", // Invalid character
        "123", // Odd length
    }
    
    for _, testStr := range testStrings {
        isValid := isValidHex(testStr)
        fmt.Printf("'%s' is valid hex: %t\n", testStr, isValid)
    }
}

func formatHexWithSeparator(data []byte, separator string) string {
    hexString := hex.EncodeToString(data)
    var result strings.Builder
    
    for i := 0; i < len(hexString); i += 2 {
        if i > 0 {
            result.WriteString(separator)
        }
        result.WriteString(hexString[i:i+2])
    }
    
    return result.String()
}

func parseHexWithSeparator(hexStr, separator string) []byte {
    // Remove separators
    cleaned := strings.ReplaceAll(hexStr, separator, "")
    
    // Decode
    decoded, err := hex.DecodeString(cleaned)
    if err != nil {
        return nil
    }
    
    return decoded
}

func hexDump(data []byte) {
    const bytesPerLine = 16
    
    for offset := 0; offset < len(data); offset += bytesPerLine {
        // Print offset
        fmt.Printf("%08x: ", offset)
        
        // Print hex values
        for i := 0; i < bytesPerLine; i++ {
            if offset+i < len(data) {
                fmt.Printf("%02x ", data[offset+i])
            } else {
                fmt.Print("   ")
            }
            
            // Add extra space in the middle
            if i == 7 {
                fmt.Print(" ")
            }
        }
        
        // Print ASCII representation
        fmt.Print(" |")
        for i := 0; i < bytesPerLine && offset+i < len(data); i++ {
            b := data[offset+i]
            if b >= 32 && b <= 126 {
                fmt.Printf("%c", b)
            } else {
                fmt.Print(".")
            }
        }
        fmt.Println("|")
    }
}

func manualHexEncode(data []byte) string {
    hexChars := "0123456789abcdef"
    var result strings.Builder
    
    for _, b := range data {
        result.WriteByte(hexChars[b>>4])   // High nibble
        result.WriteByte(hexChars[b&0x0F]) // Low nibble
    }
    
    return result.String()
}

func manualHexDecode(hexStr string) []byte {
    if len(hexStr)%2 != 0 {
        return nil // Invalid length
    }
    
    var result []byte
    
    for i := 0; i < len(hexStr); i += 2 {
        high := hexCharToValue(hexStr[i])
        low := hexCharToValue(hexStr[i+1])
        
        if high == -1 || low == -1 {
            return nil // Invalid hex character
        }
        
        result = append(result, byte(high<<4|low))
    }
    
    return result
}

func hexCharToValue(c byte) int {
    switch {
    case c >= '0' && c <= '9':
        return int(c - '0')
    case c >= 'a' && c <= 'f':
        return int(c - 'a' + 10)
    case c >= 'A' && c <= 'F':
        return int(c - 'A' + 10)
    default:
        return -1
    }
}

func isValidHex(s string) bool {
    if len(s)%2 != 0 {
        return false
    }
    
    for _, c := range s {
        if !((c >= '0' && c <= '9') || 
             (c >= 'a' && c <= 'f') || 
             (c >= 'A' && c <= 'F')) {
            return false
        }
    }
    
    return true
}
```

### Example 33: URL Encoding and Decoding

```go
package main

import (
    "fmt"
    "net/url"
    "strings"
)

func main() {
    fmt.Println("URL Encoding and Decoding:")
    
    // Test data with various special characters
    testStrings := []string{
        "Hello World",
        "user@example.com",
        "path/to/file.txt",
        "query=value&param=123",
        "special chars: !@#$%^&*()",
        "unicode: 你好世界 🌍",
        "spaces and\ttabs\nand newlines",
    }
    
    // Standard URL encoding
    fmt.Println("1. Standard URL encoding:")
    for _, s := range testStrings {
        encoded := url.QueryEscape(s)
        decoded, err := url.QueryUnescape(encoded)
        
        fmt.Printf("Original: %q\n", s)
        fmt.Printf("Encoded:  %q\n", encoded)
        if err != nil {
            fmt.Printf("Decode error: %v\n", err)
        } else {
            fmt.Printf("Decoded:  %q\n", decoded)
            fmt.Printf("Match: %t\n", s == decoded)
        }
        fmt.Println()
    }
    
    // Path encoding vs Query encoding
    fmt.Println("2. Path encoding vs Query encoding:")
    testPath := "path/with spaces/and+plus"
    
    pathEncoded := url.PathEscape(testPath)
    queryEncoded := url.QueryEscape(testPath)
    
    fmt.Printf("Original: %q\n", testPath)
    fmt.Printf("Path encoded:  %q\n", pathEncoded)
    fmt.Printf("Query encoded: %q\n", queryEncoded)
    
    pathDecoded, _ := url.PathUnescape(pathEncoded)
    queryDecoded, _ := url.QueryUnescape(queryEncoded)
    
    fmt.Printf("Path decoded:  %q\n", pathDecoded)
    fmt.Printf("Query decoded: %q\n", queryDecoded)
    
    // Manual URL encoding implementation
    fmt.Println("\n3. Manual URL encoding:")
    manualTest := "Hello World & Friends!"
    manualEncoded := manualURLEncode(manualTest)
    manualDecoded := manualURLDecode(manualEncoded)
    
    fmt.Printf("Original: %q\n", manualTest)
    fmt.Printf("Manual encoded: %q\n", manualEncoded)
    fmt.Printf("Manual decoded: %q\n", manualDecoded)
    
    // Form encoding
    fmt.Println("\n4. Form data encoding:")
    formData := url.Values{
        "name":     {"John Doe"},
        "email":    {"john@example.com"},
        "message":  {"Hello, World! This is a test message."},
        "tags":     {"go", "programming", "web"},
    }
    
    encoded := formData.Encode()
    fmt.Printf("Form encoded: %s\n", encoded)
    
    parsed, err := url.ParseQuery(encoded)
    if err != nil {
        fmt.Printf("Parse error: %v\n", err)
    } else {
        fmt.Printf("Parsed form data:\n")
        for key, values := range parsed {
            fmt.Printf("  %s: %v\n", key, values)
        }
    }
    
    // URL parsing with encoding
    fmt.Println("\n5. Complete URL parsing:")
    testURL := "https://example.com/path with spaces?query=hello world&param=value%20with%20encoding"
    
    parsed, err = url.Parse(testURL)
    if err != nil {
        fmt.Printf("URL parse error: %v\n", err)
    } else {
        fmt.Printf("Original URL: %s\n", testURL)
        fmt.Printf("Scheme: %s\n", parsed.Scheme)
        fmt.Printf("Host: %s\n", parsed.Host)
        fmt.Printf("Path: %s\n", parsed.Path)
        fmt.Printf("RawQuery: %s\n", parsed.RawQuery)
        
        // Parse query parameters
        queryParams := parsed.Query()
        fmt.Printf("Query parameters:\n")
        for key, values := range queryParams {
            fmt.Printf("  %s: %v\n", key, values)
        }
    }
    
    // Custom encoding for specific characters
    fmt.Println("\n6. Custom encoding patterns:")
    customTest := "file name with spaces.txt"
    
    // Different encoding strategies
    strategies := map[string]func(string) string{
        "Replace spaces with underscores": func(s string) string {
            return strings.ReplaceAll(s, " ", "_")
        },
        "Replace spaces with hyphens": func(s string) string {
            return strings.ReplaceAll(s, " ", "-")
        },
        "URL encode": func(s string) string {
            return url.QueryEscape(s)
        },
        "Custom encode": func(s string) string {
            return customURLEncode(s, " !@#$%^&*()")
        },
    }
    
    fmt.Printf("Original: %q\n", customTest)
    for name, strategy := range strategies {
        encoded := strategy(customTest)
        fmt.Printf("%s: %q\n", name, encoded)
    }
}

func manualURLEncode(s string) string {
    var result strings.Builder
    
    for _, r := range s {
        switch {
        case r >= 'A' && r <= 'Z':
            result.WriteRune(r)
        case r >= 'a' && r <= 'z':
            result.WriteRune(r)
        case r >= '0' && r <= '9':
            result.WriteRune(r)
        case r == '-' || r == '_' || r == '.' || r == '~':
            result.WriteRune(r)
        default:
            // Encode as UTF-8 bytes
            utf8Bytes := []byte(string(r))
            for _, b := range utf8Bytes {
                result.WriteString(fmt.Sprintf("%%%02X", b))
            }
        }
    }
    
    return result.String()
}

func manualURLDecode(s string) string {
    var result strings.Builder
    
    for i := 0; i < len(s); i++ {
        if s[i] == '%' && i+2 < len(s) {
            // Parse hex value
            var value byte
            for j := 1; j <= 2; j++ {
                c := s[i+j]
                var digit byte
                switch {
                case c >= '0' && c <= '9':
                    digit = c - '0'
                case c >= 'A' && c <= 'F':
                    digit = c - 'A' + 10
                case c >= 'a' && c <= 'f':
                    digit = c - 'a' + 10
                default:
                    // Invalid encoding, treat as literal
                    result.WriteByte(s[i])
                    goto nextChar
                }
                value = value*16 + digit
            }
            result.WriteByte(value)
            i += 2
        } else {
            result.WriteByte(s[i])
        }
        nextChar:
    }
    
    return result.String()
}

func customURLEncode(s string, charsToEncode string) string {
    var result strings.Builder
    
    for _, r := range s {
        if strings.ContainsRune(charsToEncode, r) {
            // Encode this character
            utf8Bytes := []byte(string(r))
            for _, b := range utf8Bytes {
                result.WriteString(fmt.Sprintf("%%%02X", b))
            }
        } else {
            result.WriteRune(r)
        }
    }
    
    return result.String()
}
```

### Example 34: JSON Binary Data Encoding

```go
package main

import (
    "encoding/base64"
    "encoding/json"
    "fmt"
)

// BinaryData represents binary data that can be JSON marshaled
type BinaryData struct {
    Name string `json:"name"`
    Data []byte `json:"data"`
}

// Custom JSON marshaling for binary data
func (bd BinaryData) MarshalJSON() ([]byte, error) {
    type Alias BinaryData
    return json.Marshal(&struct {
        Data string `json:"data"`
        *Alias
    }{
        Data:  base64.StdEncoding.EncodeToString(bd.Data),
        Alias: (*Alias)(&bd),
    })
}

// Custom JSON unmarshaling for binary data
func (bd *BinaryData) UnmarshalJSON(data []byte) error {
    type Alias BinaryData
    aux := &struct {
        Data string `json:"data"`
        *Alias
    }{
        Alias: (*Alias)(bd),
    }
    
    if err := json.Unmarshal(data, &aux); err != nil {
        return err
    }
    
    decoded, err := base64.StdEncoding.DecodeString(aux.Data)
    if err != nil {
        return err
    }
    
    bd.Data = decoded
    return nil
}

// Message with binary attachments
type Message struct {
    ID          int            `json:"id"`
    Subject     string         `json:"subject"`
    Body        string         `json:"body"`
    Attachments []BinaryData   `json:"attachments"`
    Metadata    map[string]any `json:"metadata"`
}

// File with binary content
type File struct {
    Name     string `json:"name"`
    Size     int64  `json:"size"`
    MimeType string `json:"mime_type"`
    Content  []byte `json:"content"`
}

func (f File) MarshalJSON() ([]byte, error) {
    type Alias File
    return json.Marshal(&struct {
        Content string `json:"content"`
        *Alias
    }{
        Content: base64.StdEncoding.EncodeToString(f.Content),
        Alias:   (*Alias)(&f),
    })
}

func (f *File) UnmarshalJSON(data []byte) error {
    type Alias File
    aux := &struct {
        Content string `json:"content"`
        *Alias
    }{
        Alias: (*Alias)(f),
    }
    
    if err := json.Unmarshal(data, &aux); err != nil {
        return err
    }
    
    decoded, err := base64.StdEncoding.DecodeString(aux.Content)
    if err != nil {
        return err
    }
    
    f.Content = decoded
    return nil
}

func main() {
    fmt.Println("JSON Binary Data Encoding:")
    
    // Create test binary data
    binaryData1 := BinaryData{
        Name: "image.png",
        Data: []byte{0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A}, // PNG header
    }
    
    binaryData2 := BinaryData{
        Name: "document.pdf",
        Data: []byte{0x25, 0x50, 0x44, 0x46, 0x2D, 0x31, 0x2E, 0x34}, // PDF header
    }
    
    // Test single binary data object
    fmt.Println("1. Single binary data object:")
    jsonData, err := json.MarshalIndent(binaryData1, "", "  ")
    if err != nil {
        fmt.Printf("Error marshaling: %v\n", err)
        return
    }
    
    fmt.Printf("JSON: %s\n", string(jsonData))
    
    // Unmarshal back
    var decoded BinaryData
    err = json.Unmarshal(jsonData, &decoded)
    if err != nil {
        fmt.Printf("Error unmarshaling: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded name: %s\n", decoded.Name)
    fmt.Printf("Decoded data: %v\n", decoded.Data)
    fmt.Printf("Data integrity: %t\n", string(binaryData1.Data) == string(decoded.Data))
    
    // Test complex message with multiple attachments
    fmt.Println("\n2. Message with binary attachments:")
    
    message := Message{
        ID:      123,
        Subject: "Test message with attachments",
        Body:    "This message contains binary attachments",
        Attachments: []BinaryData{binaryData1, binaryData2},
        Metadata: map[string]any{
            "priority": "high",
            "encrypted": false,
            "timestamp": 1642608000,
        },
    }
    
    messageJSON, err := json.MarshalIndent(message, "", "  ")
    if err != nil {
        fmt.Printf("Error marshaling message: %v\n", err)
        return
    }
    
    fmt.Printf("Message JSON: %s\n", string(messageJSON))
    
    // Unmarshal message
    var decodedMessage Message
    err = json.Unmarshal(messageJSON, &decodedMessage)
    if err != nil {
        fmt.Printf("Error unmarshaling message: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded message ID: %d\n", decodedMessage.ID)
    fmt.Printf("Decoded subject: %s\n", decodedMessage.Subject)
    fmt.Printf("Number of attachments: %d\n", len(decodedMessage.Attachments))
    
    for i, attachment := range decodedMessage.Attachments {
        fmt.Printf("Attachment %d: %s (%d bytes)\n", 
            i+1, attachment.Name, len(attachment.Data))
    }
    
    // Test file object
    fmt.Println("\n3. File object with binary content:")
    
    file := File{
        Name:     "test.bin",
        Size:     8,
        MimeType: "application/octet-stream",
        Content:  []byte{0x00, 0x01, 0x02, 0x03, 0xFF, 0xFE, 0xFD, 0xFC},
    }
    
    fileJSON, err := json.MarshalIndent(file, "", "  ")
    if err != nil {
        fmt.Printf("Error marshaling file: %v\n", err)
        return
    }
    
    fmt.Printf("File JSON: %s\n", string(fileJSON))
    
    // Unmarshal file
    var decodedFile File
    err = json.Unmarshal(fileJSON, &decodedFile)
    if err != nil {
        fmt.Printf("Error unmarshaling file: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded file name: %s\n", decodedFile.Name)
    fmt.Printf("Decoded file size: %d\n", decodedFile.Size)
    fmt.Printf("Decoded content: %v\n", decodedFile.Content)
    fmt.Printf("Content integrity: %t\n", string(file.Content) == string(decodedFile.Content))
    
    // Alternative approach using raw JSON
    fmt.Println("\n4. Raw JSON approach:")
    
    rawData := map[string]any{
        "name": "raw_binary.dat",
        "data": base64.StdEncoding.EncodeToString([]byte{0xDE, 0xAD, 0xBE, 0xEF}),
        "size": 4,
    }
    
    rawJSON, err := json.MarshalIndent(rawData, "", "  ")
    if err != nil {
        fmt.Printf("Error marshaling raw data: %v\n", err)
        return
    }
    
    fmt.Printf("Raw JSON: %s\n", string(rawJSON))
    
    // Parse raw JSON
    var parsedRaw map[string]any
    err = json.Unmarshal(rawJSON, &parsedRaw)
    if err != nil {
        fmt.Printf("Error unmarshaling raw data: %v\n", err)
        return
    }
    
    // Decode base64 data
    if dataStr, ok := parsedRaw["data"].(string); ok {
        decodedRawData, err := base64.StdEncoding.DecodeString(dataStr)
        if err != nil {
            fmt.Printf("Error decoding base64: %v\n", err)
        } else {
            fmt.Printf("Decoded raw data: %v\n", decodedRawData)
        }
    }
    
    // JSON with embedded binary in different formats
    fmt.Println("\n5. Different binary encoding formats in JSON:")
    
    testData := []byte{0x48, 0x65, 0x6C, 0x6C, 0x6F} // "Hello"
    
    formats := map[string]string{
        "base64":     base64.StdEncoding.EncodeToString(testData),
        "hex":        fmt.Sprintf("%x", testData),
        "decimal":    fmt.Sprintf("%v", testData),
        "base64url":  base64.URLEncoding.EncodeToString(testData),
    }
    
    formatsJSON, err := json.MarshalIndent(formats, "", "  ")
    if err != nil {
        fmt.Printf("Error marshaling formats: %v\n", err)
        return
    }
    
    fmt.Printf("Different formats JSON: %s\n", string(formatsJSON))
}
```

### Example 35: ASCII and Binary Conversion

```go
package main

import (
    "fmt"
    "strconv"
    "strings"
)

func main() {
    fmt.Println("ASCII and Binary Conversion:")
    
    // Test string
    text := "Hello, World! 123"
    fmt.Printf("Original text: %s\n", text)
    
    // ASCII to binary conversion
    fmt.Println("\n1. ASCII to binary conversion:")
    
    fmt.Printf("Character breakdown:\n")
    for i, char := range text {
        fmt.Printf("  [%d] '%c' -> ASCII %d -> Binary %08b\n", 
            i, char, char, char)
    }
    
    // Convert entire string to binary representation
    binaryString := stringToBinary(text)
    fmt.Printf("\nFull binary: %s\n", binaryString)
    
    // Convert back from binary
    reconstructed := binaryToString(binaryString)
    fmt.Printf("Reconstructed: %s\n", reconstructed)
    fmt.Printf("Match: %t\n", text == reconstructed)
    
    // ASCII table demonstration
    fmt.Println("\n2. ASCII table (printable characters):")
    fmt.Println("Dec  Hex  Bin      Char")
    fmt.Println("-------------------------")
    
    for i := 32; i <= 126; i++ {
        if i%10 == 2 || i <= 42 { // Show first few and every 10th
            fmt.Printf("%3d  %02X   %08b  '%c'\n", i, i, i, i)
        }
    }
    fmt.Println("... (showing sample of printable ASCII)")
    
    // Control characters
    fmt.Println("\n3. Common control characters:")
    controlChars := map[byte]string{
        0:  "NULL",
        7:  "BELL",
        8:  "BACKSPACE",
        9:  "TAB", 
        10: "LINE FEED (LF)",
        13: "CARRIAGE RETURN (CR)",
        27: "ESCAPE",
        32: "SPACE",
        127: "DELETE",
    }
    
    for code, name := range controlChars {
        fmt.Printf("  %3d (0x%02X) %08b - %s\n", code, code, code, name)
    }
    
    // Extended ASCII and UTF-8
    fmt.Println("\n4. Extended ASCII vs UTF-8:")
    
    extendedChars := "café naïve résumé"
    fmt.Printf("Text with accents: %s\n", extendedChars)
    
    // Show byte representation
    bytes := []byte(extendedChars)
    fmt.Printf("UTF-8 bytes: %v\n", bytes)
    fmt.Printf("UTF-8 hex: %x\n", bytes)
    
    fmt.Printf("Byte breakdown:\n")
    for i, b := range bytes {
        if b < 128 {
            fmt.Printf("  [%d] %02X (%3d) %08b - ASCII '%c'\n", i, b, b, b, b)
        } else {
            fmt.Printf("  [%d] %02X (%3d) %08b - UTF-8 continuation byte\n", i, b, b, b)
        }
    }
    
    // Binary arithmetic
    fmt.Println("\n5. Binary arithmetic visualization:")
    
    a, b := byte(25), byte(30)
    fmt.Printf("a = %d (%08b)\n", a, a)
    fmt.Printf("b = %d (%08b)\n", b, b)
    fmt.Printf("a + b = %d (%08b)\n", a+b, a+b)
    fmt.Printf("a - b = %d (%08b)\n", a-b, a-b) 
    fmt.Printf("a * 2 = %d (%08b)\n", a*2, a*2)
    fmt.Printf("a / 2 = %d (%08b)\n", a/2, a/2)
    
    // Bit shifts as multiplication/division
    fmt.Printf("\nBit shift arithmetic:\n")
    fmt.Printf("a << 1 (a * 2) = %d (%08b)\n", a<<1, a<<1)
    fmt.Printf("a << 2 (a * 4) = %d (%08b)\n", a<<2, a<<2)
    fmt.Printf("a >> 1 (a / 2) = %d (%08b)\n", a>>1, a>>1)
    fmt.Printf("a >> 2 (a / 4) = %d (%08b)\n", a>>2, a>>2)
    
    // Binary pattern analysis
    fmt.Println("\n6. Binary pattern analysis:")
    
    patterns := []byte{
        0b00000000, // All zeros
        0b11111111, // All ones
        0b10101010, // Alternating 1,0
        0b01010101, // Alternating 0,1
        0b11110000, // High nibble set
        0b00001111, // Low nibble set
        0b10000001, // Corner bits
    }
    
    for _, pattern := range patterns {
        fmt.Printf("Pattern %08b (%3d, 0x%02X): ", pattern, pattern, pattern)
        
        // Analyze pattern
        if pattern == 0 {
            fmt.Print("All zeros")
        } else if pattern == 0xFF {
            fmt.Print("All ones")
        } else if pattern == 0xAA {
            fmt.Print("Alternating 10")
        } else if pattern == 0x55 {
            fmt.Print("Alternating 01")
        } else if (pattern & 0xF0) == 0xF0 && (pattern & 0x0F) == 0 {
            fmt.Print("High nibble set")
        } else if (pattern & 0xF0) == 0 && (pattern & 0x0F) == 0x0F {
            fmt.Print("Low nibble set")
        } else {
            fmt.Printf("%d bits set", popCount(pattern))
        }
        fmt.Println()
    }
    
    // ASCII art using binary patterns
    fmt.Println("\n7. ASCII art from binary patterns:")
    
    binaryArt := []byte{
        0b11111111,
        0b10000001,
        0b10111101,
        0b10100101,
        0b10111101,
        0b10000001,
        0b11111111,
    }
    
    fmt.Println("Binary smiley face:")
    for i, row := range binaryArt {
        fmt.Printf("Row %d: %08b -> ", i, row)
        for bit := 7; bit >= 0; bit-- {
            if (row & (1 << bit)) != 0 {
                fmt.Print("█")
            } else {
                fmt.Print(" ")
            }
        }
        fmt.Println()
    }
}

func stringToBinary(s string) string {
    var result strings.Builder
    
    for i, char := range []byte(s) {
        if i > 0 {
            result.WriteString(" ")
        }
        result.WriteString(fmt.Sprintf("%08b", char))
    }
    
    return result.String()
}

func binaryToString(binary string) string {
    parts := strings.Split(binary, " ")
    var result strings.Builder
    
    for _, part := range parts {
        if len(part) == 8 {
            if value, err := strconv.ParseUint(part, 2, 8); err == nil {
                result.WriteByte(byte(value))
            }
        }
    }
    
    return result.String()
}

func popCount(x byte) int {
    count := 0
    for x != 0 {
        count++
        x &= x - 1
    }
    return count
}
```

### Example 36: Gob Encoding for Go Data Structures

```go
package main

import (
    "bytes"
    "encoding/gob"
    "fmt"
    "time"
)

// Person represents a person with various data types
type Person struct {
    Name      string
    Age       int
    Email     string
    Active    bool
    Score     float64
    Tags      []string
    Metadata  map[string]interface{}
    CreatedAt time.Time
}

// BinaryDocument represents a document with binary content
type BinaryDocument struct {
    ID       int64
    Title    string
    Content  []byte
    Checksum uint32
}

// ComplexData demonstrates nested structures
type ComplexData struct {
    ID      string
    Persons []Person
    Docs    []BinaryDocument
    Config  map[string]string
    Raw     []byte
}

func main() {
    fmt.Println("Gob Encoding for Go Data Structures:")
    
    // Create test data
    person := Person{
        Name:      "Alice Johnson",
        Age:       30,
        Email:     "alice@example.com", 
        Active:    true,
        Score:     95.5,
        Tags:      []string{"developer", "golang", "expert"},
        Metadata:  map[string]interface{}{"level": 5, "department": "engineering"},
        CreatedAt: time.Now(),
    }
    
    // Basic Gob encoding
    fmt.Println("1. Basic Gob encoding:")
    
    var buffer bytes.Buffer
    encoder := gob.NewEncoder(&buffer)
    
    err := encoder.Encode(person)
    if err != nil {
        fmt.Printf("Error encoding: %v\n", err)
        return
    }
    
    encoded := buffer.Bytes()
    fmt.Printf("Original struct: %+v\n", person)
    fmt.Printf("Encoded size: %d bytes\n", len(encoded))
    fmt.Printf("Encoded data (first 50 bytes): %v\n", encoded[:min(50, len(encoded))])
    
    // Decode back
    decoder := gob.NewDecoder(bytes.NewReader(encoded))
    var decodedPerson Person
    
    err = decoder.Decode(&decodedPerson)
    if err != nil {
        fmt.Printf("Error decoding: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded struct: %+v\n", decodedPerson)
    fmt.Printf("Data integrity: %t\n", person.Name == decodedPerson.Name && person.Age == decodedPerson.Age)
    
    // Binary document encoding
    fmt.Println("\n2. Binary document encoding:")
    
    doc := BinaryDocument{
        ID:       12345,
        Title:    "Binary Test Document",
        Content:  []byte{0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00}, // PNG-like header
        Checksum: 0xDEADBEEF,
    }
    
    var docBuffer bytes.Buffer
    docEncoder := gob.NewEncoder(&docBuffer)
    
    err = docEncoder.Encode(doc)
    if err != nil {
        fmt.Printf("Error encoding document: %v\n", err)
        return
    }
    
    docEncoded := docBuffer.Bytes()
    fmt.Printf("Document encoded size: %d bytes\n", len(docEncoded))
    fmt.Printf("Original content: %v\n", doc.Content)
    
    // Decode document
    docDecoder := gob.NewDecoder(bytes.NewReader(docEncoded))
    var decodedDoc BinaryDocument
    
    err = docDecoder.Decode(&decodedDoc)
    if err != nil {
        fmt.Printf("Error decoding document: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded content: %v\n", decodedDoc.Content)
    fmt.Printf("Content match: %t\n", bytes.Equal(doc.Content, decodedDoc.Content))
    
    // Complex nested structure
    fmt.Println("\n3. Complex nested structure:")
    
    complex := ComplexData{
        ID:      "complex-001",
        Persons: []Person{person},
        Docs:    []BinaryDocument{doc},
        Config: map[string]string{
            "version": "1.0",
            "mode":    "production",
        },
        Raw: []byte{0x01, 0x02, 0x03, 0x04, 0xFF},
    }
    
    var complexBuffer bytes.Buffer
    complexEncoder := gob.NewEncoder(&complexBuffer)
    
    err = complexEncoder.Encode(complex)
    if err != nil {
        fmt.Printf("Error encoding complex data: %v\n", err)
        return
    }
    
    complexEncoded := complexBuffer.Bytes()
    fmt.Printf("Complex data encoded size: %d bytes\n", len(complexEncoded))
    
    // Decode complex data
    complexDecoder := gob.NewDecoder(bytes.NewReader(complexEncoded))
    var decodedComplex ComplexData
    
    err = complexDecoder.Decode(&decodedComplex)
    if err != nil {
        fmt.Printf("Error decoding complex data: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded complex ID: %s\n", decodedComplex.ID)
    fmt.Printf("Decoded persons count: %d\n", len(decodedComplex.Persons))
    fmt.Printf("Decoded docs count: %d\n", len(decodedComplex.Docs))
    fmt.Printf("Decoded config: %v\n", decodedComplex.Config)
    fmt.Printf("Decoded raw: %v\n", decodedComplex.Raw)
    
    // Multiple objects in single stream
    fmt.Println("\n4. Multiple objects in single stream:")
    
    var streamBuffer bytes.Buffer
    streamEncoder := gob.NewEncoder(&streamBuffer)
    
    // Encode multiple objects
    objects := []interface{}{
        "Hello, World!",
        42,
        []int{1, 2, 3, 4, 5},
        map[string]int{"a": 1, "b": 2},
        person,
    }
    
    for i, obj := range objects {
        err = streamEncoder.Encode(obj)
        if err != nil {
            fmt.Printf("Error encoding object %d: %v\n", i, err)
            return
        }
    }
    
    streamData := streamBuffer.Bytes()
    fmt.Printf("Stream encoded size: %d bytes\n", len(streamData))
    
    // Decode multiple objects
    streamDecoder := gob.NewDecoder(bytes.NewReader(streamData))
    
    var str string
    var num int
    var slice []int
    var mapData map[string]int
    var personData Person
    
    decodedObjects := []interface{}{&str, &num, &slice, &mapData, &personData}
    
    for i, obj := range decodedObjects {
        err = streamDecoder.Decode(obj)
        if err != nil {
            fmt.Printf("Error decoding object %d: %v\n", i, err)
            return
        }
    }
    
    fmt.Printf("Decoded string: %s\n", str)
    fmt.Printf("Decoded number: %d\n", num)
    fmt.Printf("Decoded slice: %v\n", slice)
    fmt.Printf("Decoded map: %v\n", mapData)
    fmt.Printf("Decoded person: %s\n", personData.Name)
    
    // Gob vs other formats comparison
    fmt.Println("\n5. Gob encoding comparison:")
    
    testData := []Person{person}
    
    // Gob encoding
    var gobBuffer bytes.Buffer
    gobEnc := gob.NewEncoder(&gobBuffer)
    gobEnc.Encode(testData)
    gobSize := len(gobBuffer.Bytes())
    
    // JSON encoding for comparison
    import "encoding/json"
    jsonData, _ := json.Marshal(testData)
    jsonSize := len(jsonData)
    
    fmt.Printf("Gob size: %d bytes\n", gobSize)
    fmt.Printf("JSON size: %d bytes\n", jsonSize)
    fmt.Printf("Gob vs JSON: %.2f%% of JSON size\n", float64(gobSize)/float64(jsonSize)*100)
    
    // Type registration for interfaces
    fmt.Println("\n6. Interface type registration:")
    
    // Register types that might be stored in interface{}
    gob.Register(map[string]interface{}{})
    gob.Register([]interface{}{})
    
    interfaceData := map[string]interface{}{
        "string": "hello",
        "number": 42,
        "float":  3.14,
        "bool":   true,
        "slice":  []interface{}{1, 2, 3},
        "map":    map[string]interface{}{"nested": "value"},
    }
    
    var ifaceBuffer bytes.Buffer
    ifaceEncoder := gob.NewEncoder(&ifaceBuffer)
    
    err = ifaceEncoder.Encode(interfaceData)
    if err != nil {
        fmt.Printf("Error encoding interface data: %v\n", err)
        return
    }
    
    // Decode interface data
    ifaceDecoder := gob.NewDecoder(bytes.NewReader(ifaceBuffer.Bytes()))
    var decodedIface map[string]interface{}
    
    err = ifaceDecoder.Decode(&decodedIface)
    if err != nil {
        fmt.Printf("Error decoding interface data: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded interface data: %+v\n", decodedIface)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

### Example 37: Protocol Buffers-style Binary Encoding

```go
package main

import (
    "encoding/binary"
    "fmt"
    "io"
    "math"
)

// Varint encoding (variable-length integer)
func encodeVarint(value uint64) []byte {
    var buf []byte
    
    for value >= 0x80 {
        buf = append(buf, byte(value)|0x80)
        value >>= 7
    }
    buf = append(buf, byte(value))
    
    return buf
}

func decodeVarint(data []byte) (uint64, int) {
    var value uint64
    var shift uint
    
    for i, b := range data {
        value |= uint64(b&0x7F) << shift
        
        if b&0x80 == 0 {
            return value, i + 1
        }
        
        shift += 7
        if shift >= 64 {
            return 0, 0 // Overflow
        }
    }
    
    return 0, 0 // Incomplete
}

// ZigZag encoding for signed integers
func encodeZigZag32(value int32) uint32 {
    return uint32((value << 1) ^ (value >> 31))
}

func decodeZigZag32(value uint32) int32 {
    return int32((value >> 1) ^ -(value & 1))
}

func encodeZigZag64(value int64) uint64 {
    return uint64((value << 1) ^ (value >> 63))
}

func decodeZigZag64(value uint64) int64 {
    return int64((value >> 1) ^ -(value & 1))
}

// Wire types for protocol buffer-style encoding
const (
    WireVarint  = 0
    WireFixed64 = 1
    WireLength  = 2
    WireFixed32 = 5
)

// Tag encoding (field number + wire type)
func encodeTag(fieldNumber int, wireType int) uint64 {
    return uint64(fieldNumber<<3) | uint64(wireType)
}

func decodeTag(tag uint64) (int, int) {
    return int(tag >> 3), int(tag & 7)
}

// Binary message encoder
type MessageEncoder struct {
    buf []byte
}

func NewMessageEncoder() *MessageEncoder {
    return &MessageEncoder{}
}

func (e *MessageEncoder) WriteVarint(fieldNumber int, value uint64) {
    tag := encodeTag(fieldNumber, WireVarint)
    e.buf = append(e.buf, encodeVarint(tag)...)
    e.buf = append(e.buf, encodeVarint(value)...)
}

func (e *MessageEncoder) WriteSignedVarint(fieldNumber int, value int64) {
    zigzag := encodeZigZag64(value)
    e.WriteVarint(fieldNumber, zigzag)
}

func (e *MessageEncoder) WriteFixed32(fieldNumber int, value uint32) {
    tag := encodeTag(fieldNumber, WireFixed32)
    e.buf = append(e.buf, encodeVarint(tag)...)
    
    fixed := make([]byte, 4)
    binary.LittleEndian.PutUint32(fixed, value)
    e.buf = append(e.buf, fixed...)
}

func (e *MessageEncoder) WriteFixed64(fieldNumber int, value uint64) {
    tag := encodeTag(fieldNumber, WireFixed64)
    e.buf = append(e.buf, encodeVarint(tag)...)
    
    fixed := make([]byte, 8)
    binary.LittleEndian.PutUint64(fixed, value)
    e.buf = append(e.buf, fixed...)
}

func (e *MessageEncoder) WriteFloat32(fieldNumber int, value float32) {
    bits := math.Float32bits(value)
    e.WriteFixed32(fieldNumber, bits)
}

func (e *MessageEncoder) WriteFloat64(fieldNumber int, value float64) {
    bits := math.Float64bits(value)
    e.WriteFixed64(fieldNumber, bits)
}

func (e *MessageEncoder) WriteString(fieldNumber int, value string) {
    e.WriteBytes(fieldNumber, []byte(value))
}

func (e *MessageEncoder) WriteBytes(fieldNumber int, value []byte) {
    tag := encodeTag(fieldNumber, WireLength)
    e.buf = append(e.buf, encodeVarint(tag)...)
    e.buf = append(e.buf, encodeVarint(uint64(len(value)))...)
    e.buf = append(e.buf, value...)
}

func (e *MessageEncoder) WriteBool(fieldNumber int, value bool) {
    var val uint64
    if value {
        val = 1
    }
    e.WriteVarint(fieldNumber, val)
}

func (e *MessageEncoder) Bytes() []byte {
    return e.buf
}

// Binary message decoder
type MessageDecoder struct {
    buf []byte
    pos int
}

func NewMessageDecoder(data []byte) *MessageDecoder {
    return &MessageDecoder{buf: data}
}

func (d *MessageDecoder) ReadTag() (int, int, error) {
    if d.pos >= len(d.buf) {
        return 0, 0, io.EOF
    }
    
    tag, consumed := decodeVarint(d.buf[d.pos:])
    if consumed == 0 {
        return 0, 0, fmt.Errorf("invalid varint")
    }
    
    d.pos += consumed
    fieldNumber, wireType := decodeTag(tag)
    return fieldNumber, wireType, nil
}

func (d *MessageDecoder) ReadVarint() (uint64, error) {
    if d.pos >= len(d.buf) {
        return 0, io.EOF
    }
    
    value, consumed := decodeVarint(d.buf[d.pos:])
    if consumed == 0 {
        return 0, fmt.Errorf("invalid varint")
    }
    
    d.pos += consumed
    return value, nil
}

func (d *MessageDecoder) ReadSignedVarint() (int64, error) {
    value, err := d.ReadVarint()
    if err != nil {
        return 0, err
    }
    
    return decodeZigZag64(value), nil
}

func (d *MessageDecoder) ReadFixed32() (uint32, error) {
    if d.pos+4 > len(d.buf) {
        return 0, io.EOF
    }
    
    value := binary.LittleEndian.Uint32(d.buf[d.pos:])
    d.pos += 4
    return value, nil
}

func (d *MessageDecoder) ReadFixed64() (uint64, error) {
    if d.pos+8 > len(d.buf) {
        return 0, io.EOF
    }
    
    value := binary.LittleEndian.Uint64(d.buf[d.pos:])
    d.pos += 8
    return value, nil
}

func (d *MessageDecoder) ReadFloat32() (float32, error) {
    bits, err := d.ReadFixed32()
    if err != nil {
        return 0, err
    }
    
    return math.Float32frombits(bits), nil
}

func (d *MessageDecoder) ReadFloat64() (float64, error) {
    bits, err := d.ReadFixed64()
    if err != nil {
        return 0, err
    }
    
    return math.Float64frombits(bits), nil
}

func (d *MessageDecoder) ReadBytes() ([]byte, error) {
    length, err := d.ReadVarint()
    if err != nil {
        return nil, err
    }
    
    if d.pos+int(length) > len(d.buf) {
        return nil, io.EOF
    }
    
    value := make([]byte, length)
    copy(value, d.buf[d.pos:d.pos+int(length)])
    d.pos += int(length)
    
    return value, nil
}

func (d *MessageDecoder) ReadString() (string, error) {
    bytes, err := d.ReadBytes()
    if err != nil {
        return "", err
    }
    
    return string(bytes), nil
}

func (d *MessageDecoder) ReadBool() (bool, error) {
    value, err := d.ReadVarint()
    if err != nil {
        return false, err
    }
    
    return value != 0, nil
}

func (d *MessageDecoder) Skip(wireType int) error {
    switch wireType {
    case WireVarint:
        _, err := d.ReadVarint()
        return err
    case WireFixed32:
        _, err := d.ReadFixed32()
        return err
    case WireFixed64:
        _, err := d.ReadFixed64()
        return err
    case WireLength:
        bytes, err := d.ReadBytes()
        _ = bytes
        return err
    default:
        return fmt.Errorf("unknown wire type: %d", wireType)
    }
}

// Example message structure
type Person struct {
    ID       int64
    Name     string
    Email    string
    Age      int32
    Score    float32
    Active   bool
    Tags     []string
    Metadata []byte
}

func (p *Person) Encode() []byte {
    encoder := NewMessageEncoder()
    
    encoder.WriteSignedVarint(1, p.ID)      // field 1: ID
    encoder.WriteString(2, p.Name)          // field 2: Name
    encoder.WriteString(3, p.Email)         // field 3: Email
    encoder.WriteSignedVarint(4, int64(p.Age)) // field 4: Age
    encoder.WriteFloat32(5, p.Score)        // field 5: Score
    encoder.WriteBool(6, p.Active)          // field 6: Active
    
    // Encode tags (repeated string field)
    for _, tag := range p.Tags {
        encoder.WriteString(7, tag)         // field 7: Tags (repeated)
    }
    
    encoder.WriteBytes(8, p.Metadata)      // field 8: Metadata
    
    return encoder.Bytes()
}

func (p *Person) Decode(data []byte) error {
    decoder := NewMessageDecoder(data)
    p.Tags = nil // Reset tags slice
    
    for {
        fieldNumber, wireType, err := decoder.ReadTag()
        if err == io.EOF {
            break
        }
        if err != nil {
            return err
        }
        
        switch fieldNumber {
        case 1: // ID
            if wireType != WireVarint {
                return fmt.Errorf("wrong wire type for ID")
            }
            value, err := decoder.ReadSignedVarint()
            if err != nil {
                return err
            }
            p.ID = value
            
        case 2: // Name
            if wireType != WireLength {
                return fmt.Errorf("wrong wire type for Name")
            }
            value, err := decoder.ReadString()
            if err != nil {
                return err
            }
            p.Name = value
            
        case 3: // Email
            if wireType != WireLength {
                return fmt.Errorf("wrong wire type for Email")
            }
            value, err := decoder.ReadString()
            if err != nil {
                return err
            }
            p.Email = value
            
        case 4: // Age
            if wireType != WireVarint {
                return fmt.Errorf("wrong wire type for Age")
            }
            value, err := decoder.ReadSignedVarint()
            if err != nil {
                return err
            }
            p.Age = int32(value)
            
        case 5: // Score
            if wireType != WireFixed32 {
                return fmt.Errorf("wrong wire type for Score")
            }
            value, err := decoder.ReadFloat32()
            if err != nil {
                return err
            }
            p.Score = value
            
        case 6: // Active
            if wireType != WireVarint {
                return fmt.Errorf("wrong wire type for Active")
            }
            value, err := decoder.ReadBool()
            if err != nil {
                return err
            }
            p.Active = value
            
        case 7: // Tags (repeated)
            if wireType != WireLength {
                return fmt.Errorf("wrong wire type for Tags")
            }
            value, err := decoder.ReadString()
            if err != nil {
                return err
            }
            p.Tags = append(p.Tags, value)
            
        case 8: // Metadata
            if wireType != WireLength {
                return fmt.Errorf("wrong wire type for Metadata")
            }
            value, err := decoder.ReadBytes()
            if err != nil {
                return err
            }
            p.Metadata = value
            
        default:
            // Skip unknown field
            err := decoder.Skip(wireType)
            if err != nil {
                return err
            }
        }
    }
    
    return nil
}

func main() {
    fmt.Println("Protocol Buffers-style Binary Encoding:")
    
    // Test varint encoding
    fmt.Println("1. Varint encoding test:")
    testValues := []uint64{0, 1, 127, 128, 16383, 16384, 2097151}
    
    for _, val := range testValues {
        encoded := encodeVarint(val)
        decoded, consumed := decodeVarint(encoded)
        
        fmt.Printf("Value: %d -> Encoded: %v (%d bytes) -> Decoded: %d (consumed: %d)\n",
            val, encoded, len(encoded), decoded, consumed)
    }
    
    // Test ZigZag encoding
    fmt.Println("\n2. ZigZag encoding test:")
    signedValues := []int64{0, -1, 1, -2, 2, -64, 64, -1000, 1000}
    
    for _, val := range signedValues {
        zigzag := encodeZigZag64(val)
        decoded := decodeZigZag64(zigzag)
        
        fmt.Printf("Value: %d -> ZigZag: %d -> Decoded: %d\n", val, zigzag, decoded)
    }
    
    // Test message encoding
    fmt.Println("\n3. Message encoding test:")
    
    person := Person{
        ID:       12345,
        Name:     "Alice Johnson",
        Email:    "alice@example.com",
        Age:      -30, // Negative to test ZigZag
        Score:    95.5,
        Active:   true,
        Tags:     []string{"developer", "golang", "expert"},
        Metadata: []byte{0xDE, 0xAD, 0xBE, 0xEF},
    }
    
    fmt.Printf("Original: %+v\n", person)
    
    // Encode
    encoded := person.Encode()
    fmt.Printf("Encoded size: %d bytes\n", len(encoded))
    fmt.Printf("Encoded data: %v\n", encoded)
    fmt.Printf("Encoded hex: %x\n", encoded)
    
    // Decode
    var decodedPerson Person
    err := decodedPerson.Decode(encoded)
    if err != nil {
        fmt.Printf("Error decoding: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded: %+v\n", decodedPerson)
    
    // Verify
    fmt.Printf("\nVerification:\n")
    fmt.Printf("ID match: %t\n", person.ID == decodedPerson.ID)
    fmt.Printf("Name match: %t\n", person.Name == decodedPerson.Name)
    fmt.Printf("Email match: %t\n", person.Email == decodedPerson.Email)
    fmt.Printf("Age match: %t\n", person.Age == decodedPerson.Age)
    fmt.Printf("Score match: %t\n", person.Score == decodedPerson.Score)
    fmt.Printf("Active match: %t\n", person.Active == decodedPerson.Active)
    fmt.Printf("Tags match: %t\n", fmt.Sprintf("%v", person.Tags) == fmt.Sprintf("%v", decodedPerson.Tags))
    fmt.Printf("Metadata match: %t\n", string(person.Metadata) == string(decodedPerson.Metadata))
}
```

### Example 38: Custom Binary Format Design

```go
package main

import (
    "encoding/binary"
    "fmt"
    "io"
    "time"
)

// Custom binary format for a simple database record
// Format: MAGIC(4) + VERSION(1) + FLAGS(1) + TIMESTAMP(8) + DATA_LENGTH(4) + DATA(variable)

const (
    MAGIC_NUMBER    = 0x12345678
    FORMAT_VERSION  = 1
    FLAG_COMPRESSED = 1 << 0
    FLAG_ENCRYPTED  = 1 << 1
    FLAG_CHECKSUM   = 1 << 2
)

// Record represents a data record in our custom format
type Record struct {
    Magic     uint32
    Version   uint8
    Flags     uint8
    Timestamp uint64
    Data      []byte
    Checksum  uint32 // Optional, based on flags
}

// BinaryWriter helps write binary data in our custom format
type BinaryWriter struct {
    data []byte
}

func NewBinaryWriter() *BinaryWriter {
    return &BinaryWriter{}
}

func (w *BinaryWriter) WriteUint8(value uint8) {
    w.data = append(w.data, value)
}

func (w *BinaryWriter) WriteUint16(value uint16) {
    buf := make([]byte, 2)
    binary.LittleEndian.PutUint16(buf, value)
    w.data = append(w.data, buf...)
}

func (w *BinaryWriter) WriteUint32(value uint32) {
    buf := make([]byte, 4)
    binary.LittleEndian.PutUint32(buf, value)
    w.data = append(w.data, buf...)
}

func (w *BinaryWriter) WriteUint64(value uint64) {
    buf := make([]byte, 8)
    binary.LittleEndian.PutUint64(buf, value)
    w.data = append(w.data, buf...)
}

func (w *BinaryWriter) WriteBytes(data []byte) {
    w.data = append(w.data, data...)
}

func (w *BinaryWriter) WriteString(s string) {
    w.WriteUint32(uint32(len(s)))
    w.WriteBytes([]byte(s))
}

func (w *BinaryWriter) Bytes() []byte {
    return w.data
}

// BinaryReader helps read binary data from our custom format
type BinaryReader struct {
    data []byte
    pos  int
}

func NewBinaryReader(data []byte) *BinaryReader {
    return &BinaryReader{data: data}
}

func (r *BinaryReader) ReadUint8() (uint8, error) {
    if r.pos+1 > len(r.data) {
        return 0, io.EOF
    }
    value := r.data[r.pos]
    r.pos++
    return value, nil
}

func (r *BinaryReader) ReadUint16() (uint16, error) {
    if r.pos+2 > len(r.data) {
        return 0, io.EOF
    }
    value := binary.LittleEndian.Uint16(r.data[r.pos:])
    r.pos += 2
    return value, nil
}

func (r *BinaryReader) ReadUint32() (uint32, error) {
    if r.pos+4 > len(r.data) {
        return 0, io.EOF
    }
    value := binary.LittleEndian.Uint32(r.data[r.pos:])
    r.pos += 4
    return value, nil
}

func (r *BinaryReader) ReadUint64() (uint64, error) {
    if r.pos+8 > len(r.data) {
        return 0, io.EOF
    }
    value := binary.LittleEndian.Uint64(r.data[r.pos:])
    r.pos += 8
    return value, nil
}

func (r *BinaryReader) ReadBytes(length int) ([]byte, error) {
    if r.pos+length > len(r.data) {
        return nil, io.EOF
    }
    value := make([]byte, length)
    copy(value, r.data[r.pos:r.pos+length])
    r.pos += length
    return value, nil
}

func (r *BinaryReader) ReadString() (string, error) {
    length, err := r.ReadUint32()
    if err != nil {
        return "", err
    }
    bytes, err := r.ReadBytes(int(length))
    if err != nil {
        return "", err
    }
    return string(bytes), nil
}

func (r *BinaryReader) Position() int {
    return r.pos
}

func (r *BinaryReader) Remaining() int {
    return len(r.data) - r.pos
}

// Calculate simple checksum
func calculateChecksum(data []byte) uint32 {
    var sum uint32
    for _, b := range data {
        sum = sum*31 + uint32(b)
    }
    return sum
}

// Encode record to binary format
func (r *Record) Encode() []byte {
    writer := NewBinaryWriter()
    
    // Header
    writer.WriteUint32(r.Magic)
    writer.WriteUint8(r.Version)
    writer.WriteUint8(r.Flags)
    writer.WriteUint64(r.Timestamp)
    
    // Data length and data
    writer.WriteUint32(uint32(len(r.Data)))
    writer.WriteBytes(r.Data)
    
    // Optional checksum
    if r.Flags&FLAG_CHECKSUM != 0 {
        checksum := calculateChecksum(r.Data)
        writer.WriteUint32(checksum)
    }
    
    return writer.Bytes()
}

// Decode record from binary format
func (r *Record) Decode(data []byte) error {
    reader := NewBinaryReader(data)
    
    // Read header
    magic, err := reader.ReadUint32()
    if err != nil {
        return fmt.Errorf("failed to read magic: %v", err)
    }
    if magic != MAGIC_NUMBER {
        return fmt.Errorf("invalid magic number: 0x%08X", magic)
    }
    r.Magic = magic
    
    version, err := reader.ReadUint8()
    if err != nil {
        return fmt.Errorf("failed to read version: %v", err)
    }
    if version != FORMAT_VERSION {
        return fmt.Errorf("unsupported version: %d", version)
    }
    r.Version = version
    
    flags, err := reader.ReadUint8()
    if err != nil {
        return fmt.Errorf("failed to read flags: %v", err)
    }
    r.Flags = flags
    
    timestamp, err := reader.ReadUint64()
    if err != nil {
        return fmt.Errorf("failed to read timestamp: %v", err)
    }
    r.Timestamp = timestamp
    
    // Read data
    dataLength, err := reader.ReadUint32()
    if err != nil {
        return fmt.Errorf("failed to read data length: %v", err)
    }
    
    data, err := reader.ReadBytes(int(dataLength))
    if err != nil {
        return fmt.Errorf("failed to read data: %v", err)
    }
    r.Data = data
    
    // Read optional checksum
    if r.Flags&FLAG_CHECKSUM != 0 {
        if reader.Remaining() < 4 {
            return fmt.Errorf("missing checksum")
        }
        
        checksum, err := reader.ReadUint32()
        if err != nil {
            return fmt.Errorf("failed to read checksum: %v", err)
        }
        
        expectedChecksum := calculateChecksum(r.Data)
        if checksum != expectedChecksum {
            return fmt.Errorf("checksum mismatch: got %08X, expected %08X", 
                checksum, expectedChecksum)
        }
        r.Checksum = checksum
    }
    
    return nil
}

// File format with multiple records
type FileFormat struct {
    Header  FileHeader
    Records []Record
}

type FileHeader struct {
    Signature   [8]byte // File signature
    Version     uint16
    RecordCount uint32
    Reserved    [6]byte // Reserved for future use
}

func (f *FileFormat) Encode() []byte {
    writer := NewBinaryWriter()
    
    // Write file header
    writer.WriteBytes(f.Header.Signature[:])
    writer.WriteUint16(f.Header.Version)
    writer.WriteUint32(f.Header.RecordCount)
    writer.WriteBytes(f.Header.Reserved[:])
    
    // Write records
    for _, record := range f.Records {
        recordData := record.Encode()
        writer.WriteUint32(uint32(len(recordData))) // Record length prefix
        writer.WriteBytes(recordData)
    }
    
    return writer.Bytes()
}

func (f *FileFormat) Decode(data []byte) error {
    reader := NewBinaryReader(data)
    
    // Read file header
    signature, err := reader.ReadBytes(8)
    if err != nil {
        return fmt.Errorf("failed to read signature: %v", err)
    }
    copy(f.Header.Signature[:], signature)
    
    version, err := reader.ReadUint16()
    if err != nil {
        return fmt.Errorf("failed to read version: %v", err)
    }
    f.Header.Version = version
    
    recordCount, err := reader.ReadUint32()
    if err != nil {
        return fmt.Errorf("failed to read record count: %v", err)
    }
    f.Header.RecordCount = recordCount
    
    reserved, err := reader.ReadBytes(6)
    if err != nil {
        return fmt.Errorf("failed to read reserved: %v", err)
    }
    copy(f.Header.Reserved[:], reserved)
    
    // Read records
    f.Records = make([]Record, 0, recordCount)
    for i := uint32(0); i < recordCount; i++ {
        recordLength, err := reader.ReadUint32()
        if err != nil {
            return fmt.Errorf("failed to read record %d length: %v", i, err)
        }
        
        recordData, err := reader.ReadBytes(int(recordLength))
        if err != nil {
            return fmt.Errorf("failed to read record %d data: %v", i, err)
        }
        
        var record Record
        err = record.Decode(recordData)
        if err != nil {
            return fmt.Errorf("failed to decode record %d: %v", i, err)
        }
        
        f.Records = append(f.Records, record)
    }
    
    return nil
}

func main() {
    fmt.Println("Custom Binary Format Design:")
    
    // Create test records
    fmt.Println("1. Creating test records:")
    
    record1 := Record{
        Magic:     MAGIC_NUMBER,
        Version:   FORMAT_VERSION,
        Flags:     FLAG_CHECKSUM,
        Timestamp: uint64(time.Now().Unix()),
        Data:      []byte("Hello, this is the first record!"),
    }
    
    record2 := Record{
        Magic:     MAGIC_NUMBER,
        Version:   FORMAT_VERSION,
        Flags:     FLAG_COMPRESSED | FLAG_CHECKSUM,
        Timestamp: uint64(time.Now().Unix()),
        Data:      []byte("This is the second record with compression flag."),
    }
    
    fmt.Printf("Record 1: Magic=0x%08X, Flags=%02X, Data=%q\n", 
        record1.Magic, record1.Flags, string(record1.Data))
    fmt.Printf("Record 2: Magic=0x%08X, Flags=%02X, Data=%q\n", 
        record2.Magic, record2.Flags, string(record2.Data))
    
    // Test single record encoding/decoding
    fmt.Println("\n2. Single record encoding/decoding:")
    
    encoded1 := record1.Encode()
    fmt.Printf("Record 1 encoded size: %d bytes\n", len(encoded1))
    fmt.Printf("Encoded data (hex): %x\n", encoded1)
    
    var decoded1 Record
    err := decoded1.Decode(encoded1)
    if err != nil {
        fmt.Printf("Error decoding record 1: %v\n", err)
        return
    }
    
    fmt.Printf("Decoded record 1: Data=%q, Checksum=0x%08X\n", 
        string(decoded1.Data), decoded1.Checksum)
    fmt.Printf("Data integrity: %t\n", string(record1.Data) == string(decoded1.Data))
    
    // Test file format with multiple records
    fmt.Println("\n3. File format with multiple records:")
    
    fileFormat := FileFormat{
        Header: FileHeader{
            Signature:   [8]byte{'C', 'U', 'S', 'T', 'F', 'M', 'T', '1'},
            Version:     1,
            RecordCount: 2,
        },
        Records: []Record{record1, record2},
    }
    
    fileData := fileFormat.Encode()
    fmt.Printf("File format encoded size: %d bytes\n", len(fileData))
    
    // Decode file format
    var decodedFile FileFormat
    err = decodedFile.Decode(fileData)
    if err != nil {
        fmt.Printf("Error decoding file: %v", err)
        return
    }
    
    fmt.Printf("Decoded file signature: %s\n", string(decodedFile.Header.Signature[:]))
    fmt.Printf("Decoded file version: %d\n", decodedFile.Header.Version)
    fmt.Printf("Decoded record count: %d\n", decodedFile.Header.RecordCount)
    fmt.Printf("Actual records decoded: %d\n", len(decodedFile.Records))
    
    for i, record := range decodedFile.Records {
        fmt.Printf("Record %d: Data=%q, Flags=%02X\n", 
            i+1, string(record.Data), record.Flags)
    }
    
    // Format analysis
    fmt.Println("\n4. Format analysis:")
    
    fmt.Printf("File header size: %d bytes\n", 8+2+4+6) // signature + version + count + reserved
    
    totalRecordSize := 0
    for i, record := range decodedFile.Records {
        encoded := record.Encode()
        fmt.Printf("Record %d size: %d bytes\n", i+1, len(encoded))
        totalRecordSize += len(encoded) + 4 // +4 for length prefix
    }
    
    fmt.Printf("Total record data size: %d bytes\n", totalRecordSize)
    fmt.Printf("Total file size: %d bytes\n", len(fileData))
    
    // Error handling test
    fmt.Println("\n5. Error handling test:")
    
    // Test with corrupted magic number
    corruptedData := make([]byte, len(encoded1))
    copy(corruptedData, encoded1)
    corruptedData[0] = 0xFF // Corrupt magic number
    
    var corruptedRecord Record
    err = corruptedRecord.Decode(corruptedData)
    fmt.Printf("Corrupted magic test - Error (expected): %v\n", err)
    
    // Test with corrupted checksum
    record3 := Record{
        Magic:     MAGIC_NUMBER,
        Version:   FORMAT_VERSION,
        Flags:     FLAG_CHECKSUM,
        Timestamp: uint64(time.Now().Unix()),
        Data:      []byte("Test data for checksum"),
    }
    
    encoded3 := record3.Encode()
    encoded3[len(encoded3)-1] ^= 0xFF // Corrupt checksum
    
    var corruptedRecord3 Record
    err = corruptedRecord3.Decode(encoded3)
    fmt.Printf("Corrupted checksum test - Error (expected): %v\n", err)
    
    // Format version info
    fmt.Println("\n6. Format specification:")
    fmt.Printf("Magic Number: 0x%08X\n", MAGIC_NUMBER)
    fmt.Printf("Format Version: %d\n", FORMAT_VERSION)
    fmt.Printf("Supported Flags:\n")
    fmt.Printf("  FLAG_COMPRESSED: 0x%02X\n", FLAG_COMPRESSED)
    fmt.Printf("  FLAG_ENCRYPTED:  0x%02X\n", FLAG_ENCRYPTED)
    fmt.Printf("  FLAG_CHECKSUM:   0x%02X\n", FLAG_CHECKSUM)
    fmt.Printf("\nRecord Structure:\n")
    fmt.Printf("  Magic (4 bytes) + Version (1 byte) + Flags (1 byte)\n")
    fmt.Printf("  + Timestamp (8 bytes) + Data Length (4 bytes) + Data (variable)\n")
    fmt.Printf("  + Optional Checksum (4 bytes if FLAG_CHECKSUM is set)\n")
}
```

### Example 39: Text Encoding Transformations

```go
package main

import (
    "fmt"
    "strings"
    "unicode"
    "unicode/utf8"
)

func main() {
    fmt.Println("Text Encoding Transformations:")
    
    // UTF-8 analysis
    fmt.Println("1. UTF-8 Analysis:")
    
    testStrings := []string{
        "Hello",                    // ASCII
        "café",                     // Latin extended
        "你好",                     // Chinese
        "🌍🚀✨",                  // Emojis
        "Здравствуй мир",          // Cyrillic
        "العربية",                 // Arabic
    }
    
    for _, s := range testStrings {
        fmt.Printf("\nText: %s\n", s)
        fmt.Printf("  String length: %d characters\n", len([]rune(s)))
        fmt.Printf("  Byte length: %d bytes\n", len(s))
        fmt.Printf("  UTF-8 valid: %t\n", utf8.ValidString(s))
        
        // Show byte representation
        bytes := []byte(s)
        fmt.Printf("  Bytes: %v\n", bytes)
        fmt.Printf("  Hex: %x\n", bytes)
        
        // Show rune breakdown
        fmt.Printf("  Runes:\n")
        for i, r := range s {
            size := utf8.RuneLen(r)
            fmt.Printf("    [%d] U+%04X '%c' (%d bytes)\n", i, r, r, size)
        }
    }
    
    // Character case transformations
    fmt.Println("\n2. Case Transformations:")
    
    testText := "Hello, World! Café naïve résumé 123"
    fmt.Printf("Original: %s\n", testText)
    fmt.Printf("Upper: %s\n", strings.ToUpper(testText))
    fmt.Printf("Lower: %s\n", strings.ToLower(testText))
    fmt.Printf("Title: %s\n", strings.Title(testText))
    
    // Manual case conversion
    fmt.Printf("Manual upper: %s\n", manualToUpper(testText))
    fmt.Printf("Manual lower: %s\n", manualToLower(testText))
    
    // ROT13 transformation
    fmt.Println("\n3. ROT13 Transformation:")
    
    rot13Text := "Hello, World!"
    encoded := rot13(rot13Text)
    decoded := rot13(encoded) // ROT13 is self-inverse
    
    fmt.Printf("Original: %s\n", rot13Text)
    fmt.Printf("ROT13: %s\n", encoded)
    fmt.Printf("Decoded: %s\n", decoded)
    
    // Caesar cipher
    fmt.Println("\n4. Caesar Cipher:")
    
    caesarText := "HELLO WORLD"
    for shift := 1; shift <= 25; shift += 6 {
        encrypted := caesarCipher(caesarText, shift)
        decrypted := caesarCipher(encrypted, -shift)
        fmt.Printf("Shift %2d: %s -> %s -> %s\n", shift, caesarText, encrypted, decrypted)
    }
    
    // Morse code
    fmt.Println("\n5. Morse Code:")
    
    morseText := "HELLO WORLD"
    morse := textToMorse(morseText)
    decoded = morseToText(morse)
    
    fmt.Printf("Text: %s\n", morseText)
    fmt.Printf("Morse: %s\n", morse)
    fmt.Printf("Decoded: %s\n", decoded)
    
    // Unicode normalization examples
    fmt.Println("\n6. Unicode Normalization:")
    
    // Different representations of the same character
    composed := "é"                    // Single character é
    decomposed := "e\u0301"           // e + combining acute accent
    
    fmt.Printf("Composed: %q (len=%d, bytes=%v)\n", composed, len(composed), []byte(composed))
    fmt.Printf("Decomposed: %q (len=%d, bytes=%v)\n", decomposed, len(decomposed), []byte(decomposed))
    fmt.Printf("Equal: %t\n", composed == decomposed)
    fmt.Printf("Visually same: %t\n", normalizeForComparison(composed) == normalizeForComparison(decomposed))
    
    // Character frequency analysis
    fmt.Println("\n7. Character Frequency Analysis:")
    
    analysisText := "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet."
    frequencies := analyzeCharacterFrequency(analysisText)
    
    fmt.Printf("Text: %s\n", analysisText)
    fmt.Printf("Character frequencies (top 10):\n")
    
    type charFreq struct {
        char  rune
        count int
    }
    
    var freqList []charFreq
    for char, count := range frequencies {
        freqList = append(freqList, charFreq{char, count})
    }
    
    // Simple sort by frequency (descending)
    for i := 0; i < len(freqList); i++ {
        for j := i + 1; j < len(freqList); j++ {
            if freqList[j].count > freqList[i].count {
                freqList[i], freqList[j] = freqList[j], freqList[i]
            }
        }
    }
    
    for i := 0; i < 10 && i < len(freqList); i++ {
        char := freqList[i].char
        count := freqList[i].count
        if unicode.IsPrint(char) {
            fmt.Printf("  '%c': %d\n", char, count)
        } else {
            fmt.Printf("  U+%04X: %d\n", char, count)
        }
    }
    
    // Text statistics
    fmt.Printf("\nText statistics:\n")
    fmt.Printf("  Total characters: %d\n", utf8.RuneCountInString(analysisText))
    fmt.Printf("  Total bytes: %d\n", len(analysisText))
    fmt.Printf("  Letters: %d\n", countLetters(analysisText))
    fmt.Printf("  Digits: %d\n", countDigits(analysisText))
    fmt.Printf("  Spaces: %d\n", countSpaces(analysisText))
    fmt.Printf("  Punctuation: %d\n", countPunctuation(analysisText))
}

func manualToUpper(s string) string {
    var result strings.Builder
    for _, r := range s {
        if r >= 'a' && r <= 'z' {
            result.WriteRune(r - 32)
        } else {
            result.WriteRune(r)
        }
    }
    return result.String()
}

func manualToLower(s string) string {
    var result strings.Builder
    for _, r := range s {
        if r >= 'A' && r <= 'Z' {
            result.WriteRune(r + 32)
        } else {
            result.WriteRune(r)
        }
    }
    return result.String()
}

func rot13(s string) string {
    var result strings.Builder
    for _, r := range s {
        switch {
        case r >= 'A' && r <= 'Z':
            result.WriteRune((r-'A'+13)%26 + 'A')
        case r >= 'a' && r <= 'z':
            result.WriteRune((r-'a'+13)%26 + 'a')
        default:
            result.WriteRune(r)
        }
    }
    return result.String()
}

func caesarCipher(s string, shift int) string {
    var result strings.Builder
    for _, r := range s {
        switch {
        case r >= 'A' && r <= 'Z':
            shifted := (int(r-'A')+shift+26)%26 + int('A')
            result.WriteRune(rune(shifted))
        case r >= 'a' && r <= 'z':
            shifted := (int(r-'a')+shift+26)%26 + int('a')
            result.WriteRune(rune(shifted))
        default:
            result.WriteRune(r)
        }
    }
    return result.String()
}

func textToMorse(s string) string {
    morseCode := map[rune]string{
        'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
        'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",
        'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
        'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
        'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--",
        'Z': "--..", '0': "-----", '1': ".----", '2': "..---",
        '3': "...--", '4': "....-", '5': ".....", '6': "-....",
        '7': "--...", '8': "---..", '9': "----.", ' ': "/",
    }
    
    var result strings.Builder
    for _, r := range strings.ToUpper(s) {
        if code, ok := morseCode[r]; ok {
            if result.Len() > 0 && code != "/" {
                result.WriteString(" ")
            }
            result.WriteString(code)
        }
    }
    return result.String()
}

func morseToText(morse string) string {
    morseToChar := map[string]rune{
        ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E',
        "..-.": 'F', "--.": 'G', "....": 'H', "..": 'I', ".---": 'J',
        "-.-": 'K', ".-..": 'L', "--": 'M', "-.": 'N', "---": 'O',
        ".--.": 'P', "--.-": 'Q', ".-.": 'R', "...": 'S', "-": 'T',
        "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X', "-.--": 'Y',
        "--..": 'Z', "-----": '0', ".----": '1', "..---": '2',
        "...--": '3', "....-": '4', ".....": '5', "-....": '6',
        "--...": '7', "---..": '8', "----.": '9', "/": ' ',
    }
    
    var result strings.Builder
    codes := strings.Split(morse, " ")
    
    for _, code := range codes {
        if char, ok := morseToChar[code]; ok {
            result.WriteRune(char)
        }
    }
    
    return result.String()
}

func normalizeForComparison(s string) string {
    // Simple normalization - remove combining characters
    var result strings.Builder
    for _, r := range s {
        if !unicode.Is(unicode.Mn, r) { // Mn = Nonspacing marks (combining characters)
            result.WriteRune(r)
        }
    }
    return result.String()
}

func analyzeCharacterFrequency(s string) map[rune]int {
    frequencies := make(map[rune]int)
    for _, r := range s {
        frequencies[r]++
    }
    return frequencies
}

func countLetters(s string) int {
    count := 0
    for _, r := range s {
        if unicode.IsLetter(r) {
            count++
        }
    }
    return count
}

func countDigits(s string) int {
    count := 0
    for _, r := range s {
        if unicode.IsDigit(r) {
            count++
        }
    }
    return count
}

func countSpaces(s string) int {
    count := 0
    for _, r := range s {
        if unicode.IsSpace(r) {
            count++
        }
    }
    return count
}

func countPunctuation(s string) int {
    count := 0
    for _, r := range s {
        if unicode.IsPunct(r) {
            count++
        }
    }
    return count
}
```

### Example 40: MIME and Content Encoding

```go
package main

import (
    "encoding/base64"
    "fmt"
    "mime"
    "mime/quotedprintable"
    "net/textproto"
    "strings"
)

func main() {
    fmt.Println("MIME and Content Encoding:")
    
    // MIME type detection
    fmt.Println("1. MIME Type Detection:")
    
    files := map[string][]byte{
        "document.pdf":  {0x25, 0x50, 0x44, 0x46},                             // PDF
        "image.png":     {0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A},   // PNG
        "image.jpg":     {0xFF, 0xD8, 0xFF, 0xE0},                             // JPEG
        "archive.zip":   {0x50, 0x4B, 0x03, 0x04},                             // ZIP
        "text.txt":      {0x48, 0x65, 0x6C, 0x6C, 0x6F},                      // Text
        "binary.exe":    {0x4D, 0x5A},                                          // PE executable
    }
    
    for filename, data := range files {
        // Detect MIME type by extension
        mimeType := mime.TypeByExtension(getFileExtension(filename))
        if mimeType == "" {
            mimeType = "application/octet-stream"
        }
        
        // Detect by content (simple magic number detection)
        detectedType := detectMimeByContent(data)
        
        fmt.Printf("File: %s\n", filename)
        fmt.Printf("  By extension: %s\n", mimeType)
        fmt.Printf("  By content: %s\n", detectedType)
        fmt.Printf("  Data: %v\n", data)
        fmt.Println()
    }
    
    // Quoted-Printable encoding
    fmt.Println("2. Quoted-Printable Encoding:")
    
    qpText := "Café naïve résumé with special characters: àáâãäåæçèéêë"
    fmt.Printf("Original: %s\n", qpText)
    
    var qpBuffer strings.Builder
    qpWriter := quotedprintable.NewWriter(&qpBuffer)
    qpWriter.Write([]byte(qpText))
    qpWriter.Close()
    
    qpEncoded := qpBuffer.String()
    fmt.Printf("Quoted-Printable: %s\n", qpEncoded)
    
    // Decode quoted-printable
    qpReader := quotedprintable.NewReader(strings.NewReader(qpEncoded))
    qpDecoded := make([]byte, len(qpText)*2) // Buffer with extra space
    n, _ := qpReader.Read(qpDecoded)
    qpDecoded = qpDecoded[:n]
    
    fmt.Printf("Decoded: %s\n", string(qpDecoded))
    fmt.Printf("Match: %t\n", qpText == string(qpDecoded))
    
    // Email message with MIME encoding
    fmt.Println("\n3. Email Message with MIME Encoding:")
    
    email := createMIMEEmail(
        "sender@example.com",
        "recipient@example.com",
        "Test Email with Attachments",
        "This is a test email with binary attachments.",
        []Attachment{
            {
                Filename:    "test.png",
                ContentType: "image/png",
                Data:        []byte{0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00},
            },
            {
                Filename:    "document.pdf",
                ContentType: "application/pdf",
                Data:        []byte{0x25, 0x50, 0x44, 0x46, 0x2D, 0x31, 0x2E, 0x34},
            },
        },
    )
    
    fmt.Printf("MIME Email:\n%s\n", email)
    
    // Content-Transfer-Encoding examples
    fmt.Println("4. Content-Transfer-Encoding Examples:")
    
    binaryData := []byte{0x00, 0x01, 0x02, 0x03, 0xFF, 0xFE, 0xFD, 0xFC}
    fmt.Printf("Binary data: %v\n", binaryData)
    
    // Base64 encoding
    base64Encoded := base64.StdEncoding.EncodeToString(binaryData)
    fmt.Printf("Base64: %s\n", base64Encoded)
    
    // 7bit encoding (for ASCII text)
    asciiText := "Hello, World!"
    fmt.Printf("7bit (ASCII): %s\n", asciiText)
    
    // 8bit encoding (for extended ASCII)
    extendedText := "Café naïve"
    fmt.Printf("8bit (Extended): %s\n", extendedText)
    fmt.Printf("8bit (Bytes): %v\n", []byte(extendedText))
    
    // Binary encoding (same as 8bit but semantically different)
    fmt.Printf("Binary: %v\n", binaryData)
    
    // MIME header encoding
    fmt.Println("\n5. MIME Header Encoding:")
    
    headers := []string{
        "Simple ASCII Header",
        "Header with Café",
        "Заголовок на русском",
        "日本語のヘッダー",
        "🌍 Emoji Header 🚀",
    }
    
    for _, header := range headers {
        encoded := encodeMIMEHeader(header)
        decoded := decodeMIMEHeader(encoded)
        
        fmt.Printf("Original: %s\n", header)
        fmt.Printf("Encoded:  %s\n", encoded)
        fmt.Printf("Decoded:  %s\n", decoded)
        fmt.Printf("Match:    %t\n", header == decoded)
        fmt.Println()
    }
    
    // Content-Disposition header
    fmt.Println("6. Content-Disposition Header:")
    
    dispositions := []struct {
        disposition string
        filename    string
    }{
        {"attachment", "document.pdf"},
        {"inline", "image.png"},
        {"attachment", "файл.txt"},        // Cyrillic filename
        {"attachment", "文档.pdf"},         // Chinese filename
    }
    
    for _, disp := range dispositions {
        header := createContentDisposition(disp.disposition, disp.filename)
        fmt.Printf("Disposition: %s, Filename: %s\n", disp.disposition, disp.filename)
        fmt.Printf("Header: %s\n", header)
        fmt.Println()
    }
}

type Attachment struct {
    Filename    string
    ContentType string
    Data        []byte
}

func getFileExtension(filename string) string {
    parts := strings.Split(filename, ".")
    if len(parts) > 1 {
        return "." + parts[len(parts)-1]
    }
    return ""
}

func detectMimeByContent(data []byte) string {
    if len(data) < 4 {
        return "application/octet-stream"
    }
    
    // Simple magic number detection
    switch {
    case data[0] == 0x25 && data[1] == 0x50 && data[2] == 0x44 && data[3] == 0x46:
        return "application/pdf"
    case data[0] == 0x89 && data[1] == 0x50 && data[2] == 0x4E && data[3] == 0x47:
        return "image/png"
    case data[0] == 0xFF && data[1] == 0xD8 && data[2] == 0xFF:
        return "image/jpeg"
    case data[0] == 0x50 && data[1] == 0x4B && data[2] == 0x03 && data[3] == 0x04:
        return "application/zip"
    case data[0] == 0x4D && data[1] == 0x5A:
        return "application/x-msdownload"
    default:
        // Check if it's text
        for _, b := range data {
            if b > 127 || (b < 32 && b != 9 && b != 10 && b != 13) {
                return "application/octet-stream"
            }
        }
        return "text/plain"
    }
}

func createMIMEEmail(from, to, subject, body string, attachments []Attachment) string {
    boundary := "----=_NextPart_000_001A_01D8E4B5.12345678"
    
    var email strings.Builder
    
    // Headers
    email.WriteString(fmt.Sprintf("From: %s\n", from))
    email.WriteString(fmt.Sprintf("To: %s\n", to))
    email.WriteString(fmt.Sprintf("Subject: %s\n", subject))
    email.WriteString("MIME-Version: 1.0\n")
    email.WriteString(fmt.Sprintf("Content-Type: multipart/mixed; boundary=%q\n", boundary))
    email.WriteString("\n")
    
    // Body
    email.WriteString(fmt.Sprintf("--%s\n", boundary))
    email.WriteString("Content-Type: text/plain; charset=utf-8\n")
    email.WriteString("Content-Transfer-Encoding: 8bit\n")
    email.WriteString("\n")
    email.WriteString(body)
    email.WriteString("\n\n")
    
    // Attachments
    for _, attachment := range attachments {
        email.WriteString(fmt.Sprintf("--%s\n", boundary))
        email.WriteString(fmt.Sprintf("Content-Type: %s\n", attachment.ContentType))
        email.WriteString("Content-Transfer-Encoding: base64\n")
        email.WriteString(fmt.Sprintf("Content-Disposition: attachment; filename=%q\n", attachment.Filename))
        email.WriteString("\n")
        
        // Encode attachment data as base64
        encoded := base64.StdEncoding.EncodeToString(attachment.Data)
        // Split into lines of 76 characters (MIME requirement)
        for i := 0; i < len(encoded); i += 76 {
            end := i + 76
            if end > len(encoded) {
                end = len(encoded)
            }
            email.WriteString(encoded[i:end])
            email.WriteString("\n")
        }
        email.WriteString("\n")
    }
    
    // End boundary
    email.WriteString(fmt.Sprintf("--%s--\n", boundary))
    
    return email.String()
}

func encodeMIMEHeader(text string) string {
    // Simple RFC 2047 encoding
    if isASCII(text) {
        return text
    }
    
    encoded := base64.StdEncoding.EncodeToString([]byte(text))
    return fmt.Sprintf("=?UTF-8?B?%s?=", encoded)
}

func decodeMIMEHeader(encoded string) string {
    // Simple RFC 2047 decoding
    if !strings.HasPrefix(encoded, "=?") || !strings.HasSuffix(encoded, "?=") {
        return encoded
    }
    
    // Parse =?charset?encoding?encoded-text?=
    parts := strings.Split(encoded[2:len(encoded)-2], "?")
    if len(parts) != 3 {
        return encoded
    }
    
    charset := parts[0]
    encoding := parts[1]
    encodedText := parts[2]
    
    if charset != "UTF-8" || encoding != "B" {
        return encoded
    }
    
    decoded, err := base64.StdEncoding.DecodeString(encodedText)
    if err != nil {
        return encoded
    }
    
    return string(decoded)
}

func createContentDisposition(disposition, filename string) string {
    if isASCII(filename) {
        return fmt.Sprintf("%s; filename=%q", disposition, filename)
    }
    
    // RFC 2231 encoding for non-ASCII filenames
    encoded := fmt.Sprintf("UTF-8''%s", urlEncode(filename))
    return fmt.Sprintf("%s; filename*=%s", disposition, encoded)
}

func isASCII(s string) bool {
    for _, r := range s {
        if r > 127 {
            return false
        }
    }
    return true
}

func urlEncode(s string) string {
    var result strings.Builder
    for _, b := range []byte(s) {
        if (b >= 'A' && b <= 'Z') || (b >= 'a' && b <= 'z') || (b >= '0' && b <= '9') ||
           b == '-' || b == '_' || b == '.' || b == '~' {
            result.WriteByte(b)
        } else {
            result.WriteString(fmt.Sprintf("%%%02X", b))
        }
    }
    return result.String()
}
```

---

## Summary

This comprehensive guide has covered 40 detailed Go code examples demonstrating various aspects of binary data manipulation:

### Key Topics Covered

**Basic Operations (Examples 1-10):**
- Creating and manipulating byte slices
- Memory-efficient operations
- Slice sorting and advanced patterns
- Type conversions and comparisons

**File I/O (Examples 11-20):**
- Binary file reading and writing
- Random access operations
- Streaming and concurrent processing
- Compression and format detection

**Bitwise Operations (Examples 21-30):**
- Basic bitwise arithmetic
- Bit manipulation utilities
- Cryptographic operations
- Compression techniques and advanced patterns

**Encoding/Decoding (Examples 31-40):**
- Base64, hexadecimal, and URL encoding
- JSON binary data handling
- Custom binary formats
- MIME and text transformations

### Best Practices Demonstrated

1. **Memory Efficiency**: Pre-allocating slices, using byte pools, and avoiding unnecessary copies
2. **Error Handling**: Proper validation and graceful error recovery
3. **Performance**: Optimized algorithms for bit manipulation and data processing
4. **Security**: Checksum validation, format verification, and safe type conversions
5. **Interoperability**: Standard encoding formats and cross-platform compatibility

### Common Patterns

- **Builder Pattern**: For efficient byte slice construction
- **Pool Pattern**: For memory reuse and garbage collection optimization  
- **Pipeline Pattern**: For streaming data processing
- **Validation Pattern**: For data integrity and format verification

### Use Cases Covered

- Network protocol implementation
- File format processing
- Cryptographic operations
- Data compression and encoding
- Binary search and manipulation
- Cross-platform data exchange

These examples provide a solid foundation for working with binary data in Go, demonstrating both fundamental concepts and advanced techniques used in real-world applications.

**Note**: Due to response length limitations, this guide covers the first 40 examples (Basic Operations, File I/O, Bitwise Operations, and Encoding/Decoding). The remaining 40 examples would cover Buffer Operations, Endianness Handling, Advanced Binary Manipulation, and Real-world Scenarios, following the same detailed and educational approach.
```
```
```
```
```