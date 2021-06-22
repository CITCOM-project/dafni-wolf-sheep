# dafni-wolf-sheep

Can I make the mesa wolf-sheep example run on DAFNI?

## Try it:

Clone this repo:

```
git clone https://github.com/RSE-Sheffield/dafni-wolf-sheep.git
cd dafni-wolf-sheep
```

Install docker.

Build the container:

```
docker build -t dafni-wolf-sheep .
```

Run the container:

```
docker run dafni-wolf-sheep 
```

To upload to DAFNI:

```
docker build -t dafni-wolf-sheep:to-upload .
docker save -o dafni-wolf-sheep.tar dafni-wolf-sheep:to-upload
```
