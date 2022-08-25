# Pseudo normal maps generator
A utility for processing a texture using its normal map.

## What is this utility for?

Some older game engines do not support certain technologies. These technologies may include Normal Mapping - a texture mapping technique used for faking the lighting of bumps and dents. Using this utility and the existing normal map, you can process the texture and get something close to the bump mapping result. 

## Example results 

![alt text](https://github.com/mrglaster/pseudonormalmaps_generator/blob/main/demo_images/example.png?raw=true)

## In-model results

![alt text](https://github.com/mrglaster/pseudonormalmaps_generator/blob/main/demo_images/example_2.png?raw=true)

## How to use?

1) Install requirement packages

```
pip install -r requirements.txt
```

or 

```
pip install opencv_python_headless==4.6.0.66 Pillow==9.2.0
```

2) Run the utility

```
python generator.py -t texture.png -n normal_map.png 
```

## Links

https://www.moddb.com/tutorials/pseudo-normal-maps-for-gold-source-engine
