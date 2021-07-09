package main

import "golang.org/x/tour/pic"
import "image"
import "image/color"

type Image struct{
	pixels [][]color.Color
}

func (Image) ColorModel() color.Model {
	return color.RGBAModel
}

func (i Image) Bounds() image.Rectangle {
	return image.Rect(0,0, len(i.pixels[0]), len(i.pixels))
}

func (i Image) At(x, y int) color.Color {
	return i.pixels[x][y]
}

func Pic(dx, dy int) [][]color.Color {
	s := make([][]color.Color, dy)
	for x := range s {
		s[x] = make([]color.Color, dx)
		for y := 0; y < dx; y++ {
			s[x][y] = color.RGBA{uint8((x+y)/2), uint8((x+y)/2), 255, 255}
		}
	}
	return s
}

func main() {
	m := Image{Pic(256,256)}
	pic.ShowImage(m)
}
