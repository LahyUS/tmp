//***********************************************************************************************************************************\\
THIS MODEL HAS 3 MODULE, EACH ONE HAS A "mode" TO RUN CODE:

	+Color Histogram Similarity: mode = 0
	+SIFT Features Similarity: mode = 1
	+Image Similarity: mode = 2

To run model:
	+ Open command prompt
	+ cd to "..UDXLAV-DO AN-HQ29/Source code/"
	+ type this script: "python main.py --first <image_1's PATH> --second <image_2's PATH> --mode <0/1/2>"
	+...
	+Ex: python main.py --first Dataset/or1_amazon.png --second Dataset/Paypal.png --mode 2