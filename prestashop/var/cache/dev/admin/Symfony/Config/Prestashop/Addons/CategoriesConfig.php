<?php

namespace Symfony\Config\Prestashop\Addons;

require_once __DIR__.\DIRECTORY_SEPARATOR.'CategoriesConfig'.\DIRECTORY_SEPARATOR.'CategoriesConfig.php';

use Symfony\Component\Config\Loader\ParamConfigurator;
use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class CategoriesConfig 
{
    private $idCategory;
    private $name;
    private $order;
    private $link;
    private $idParent;
    private $parentLink;
    private $tab;
    private $categories;
    private $_usedProperties = [];

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function idCategory($value): static
    {
        $this->_usedProperties['idCategory'] = true;
        $this->idCategory = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function name($value): static
    {
        $this->_usedProperties['name'] = true;
        $this->name = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function order($value): static
    {
        $this->_usedProperties['order'] = true;
        $this->order = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function link($value): static
    {
        $this->_usedProperties['link'] = true;
        $this->link = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function idParent($value): static
    {
        $this->_usedProperties['idParent'] = true;
        $this->idParent = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function parentLink($value): static
    {
        $this->_usedProperties['parentLink'] = true;
        $this->parentLink = $value;

        return $this;
    }

    /**
     * @default null
     * @param ParamConfigurator|mixed $value
     * @return $this
     */
    public function tab($value): static
    {
        $this->_usedProperties['tab'] = true;
        $this->tab = $value;

        return $this;
    }

    public function categories(array $value = []): \Symfony\Config\Prestashop\Addons\CategoriesConfig\CategoriesConfig
    {
        $this->_usedProperties['categories'] = true;

        return $this->categories[] = new \Symfony\Config\Prestashop\Addons\CategoriesConfig\CategoriesConfig($value);
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('id_category', $value)) {
            $this->_usedProperties['idCategory'] = true;
            $this->idCategory = $value['id_category'];
            unset($value['id_category']);
        }

        if (array_key_exists('name', $value)) {
            $this->_usedProperties['name'] = true;
            $this->name = $value['name'];
            unset($value['name']);
        }

        if (array_key_exists('order', $value)) {
            $this->_usedProperties['order'] = true;
            $this->order = $value['order'];
            unset($value['order']);
        }

        if (array_key_exists('link', $value)) {
            $this->_usedProperties['link'] = true;
            $this->link = $value['link'];
            unset($value['link']);
        }

        if (array_key_exists('id_parent', $value)) {
            $this->_usedProperties['idParent'] = true;
            $this->idParent = $value['id_parent'];
            unset($value['id_parent']);
        }

        if (array_key_exists('parent_link', $value)) {
            $this->_usedProperties['parentLink'] = true;
            $this->parentLink = $value['parent_link'];
            unset($value['parent_link']);
        }

        if (array_key_exists('tab', $value)) {
            $this->_usedProperties['tab'] = true;
            $this->tab = $value['tab'];
            unset($value['tab']);
        }

        if (array_key_exists('categories', $value)) {
            $this->_usedProperties['categories'] = true;
            $this->categories = array_map(fn ($v) => new \Symfony\Config\Prestashop\Addons\CategoriesConfig\CategoriesConfig($v), $value['categories']);
            unset($value['categories']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['idCategory'])) {
            $output['id_category'] = $this->idCategory;
        }
        if (isset($this->_usedProperties['name'])) {
            $output['name'] = $this->name;
        }
        if (isset($this->_usedProperties['order'])) {
            $output['order'] = $this->order;
        }
        if (isset($this->_usedProperties['link'])) {
            $output['link'] = $this->link;
        }
        if (isset($this->_usedProperties['idParent'])) {
            $output['id_parent'] = $this->idParent;
        }
        if (isset($this->_usedProperties['parentLink'])) {
            $output['parent_link'] = $this->parentLink;
        }
        if (isset($this->_usedProperties['tab'])) {
            $output['tab'] = $this->tab;
        }
        if (isset($this->_usedProperties['categories'])) {
            $output['categories'] = array_map(fn ($v) => $v->toArray(), $this->categories);
        }

        return $output;
    }

}
