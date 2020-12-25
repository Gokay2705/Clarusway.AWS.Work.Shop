#!/bin/bash

getDate(){
        date
        return
}

getDate

name="Mustafa"
demLocal(){
        local name="Kara Duman"
        return
}

demLocal

echo "$name"